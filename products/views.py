from django.shortcuts import render
from products.models import Product, Images


# Create your views here.
def all_products(request):
    """ A view to show all products """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details """
    item = Product.objects.get(pk=product_id)
    images = Images.objects.filter(product_id=product_id)

    context = {
        'item': item,
        'images': images
    }

    return render(request, 'products/products_detail.html', context)
