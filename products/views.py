from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from products.models import Product, Images, Variants
from django.http import JsonResponse
from django.template.loader import render_to_string


# Create your views here.
def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria.")
                return redirect(reverse('RR_home'))

            queries = Q(title__icontains=query) | Q(detail__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details """
    product = Product.objects.get(pk=product_id)
    images = Images.objects.filter(product_id=product_id)

    context = {
        'product': product,
        'images': images
    }

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
        data = {'rendered_table': render_to_string('color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)

