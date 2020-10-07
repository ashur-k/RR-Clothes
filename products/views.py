from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductDetail


# Create your views here.


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)
    print(product.id)
    product_detail = ProductDetail.objects.filter(product=product_id)
    for detail in product_detail:
        print(detail.size)
       
    context = {
        'product': product,
        'product_detail': product_detail,
     }

    return render(request, 'products/products_detail.html', context)
