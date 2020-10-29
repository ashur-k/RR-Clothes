import json
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string
from django.db.models.functions import Lower
from products.models import Product, Images, Variants, Category
from django.db.models import Q

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


# Create your views here.
def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        print(products.count())

        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title + " > " + rs.category.title
            results.append(product_json)
            print(rs.title)
        print(results)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def product_detail(request, product_id):
    """ A view to show product details """
    query = request.GET.get('q')
    product = Product.objects.get(pk=product_id)
    images = Images.objects.filter(product_id=product_id)
    no_variant_id = None

    no_variants = Variants.objects.filter(product_id=product_id)
    for items in no_variants:
        no_variant_id = items.id

    print(no_variant_id)
    context = {
        'product': product,
        'images': images,
        'no_variant_id': no_variant_id
    }

    if product.variant != "None":  # Product have variants
        if request.method == 'POST':  # if we select color
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id)
            colors = Variants.objects.filter(product_id=product_id, size_id=variant.size_id)
            sizes = Variants.objects.raw('SELECT * FROM  products_variants  WHERE product_id=%s GROUP BY size_id', [product_id])
            query += variant.title + ' Size:' + str(variant.size) + ' Color: ' + str(variant.color)
        else:
            variants = Variants.objects.filter(product_id=product_id)
            colors = Variants.objects.filter(product_id=product_id, size_id=variants[0].size_id )
            sizes = Variants.objects.raw('SELECT * FROM  products_variants  WHERE product_id=%s GROUP BY size_id', [product_id])
            variant = Variants.objects.get(id=variants[0].id)

        context.update({
            'sizes': sizes,
            'colors': colors,
            'variant': variant,
            'query': query,
                        })
    return render(request, 'products/products_detail.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('products/color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)

