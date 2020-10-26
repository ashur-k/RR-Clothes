import json
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from products.models import Product, Images, Variants


from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


# Create your views here.
def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria.")
                return redirect(reverse('RR_home'))

            queries = Q(title__icontains=query) | Q(detail__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query
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

    context = {
        'product': product,
        'images': images,
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

