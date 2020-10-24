from django.shortcuts import render


# Create your views here.
def all_products(request):
    """ A view to show all products """

    return render(request, 'products/products.html')


def product_detail(request, product_id):
    """ A view to show product details """

    return render(request, 'products/products_detail.html')
