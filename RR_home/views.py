from django.shortcuts import render
from products.models import Product


# Create your views here.
def index(request):
    """ Index page view """
    products_slider = Product.objects.all().order_by('id')[:6]
    products_latest = Product.objects.all()
    context = {
        'products_slider': products_slider,
        'products_latest': products_latest,
    }
    return render(request, 'home/index.html', context)


