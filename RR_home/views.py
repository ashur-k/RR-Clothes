from django.shortcuts import render, HttpResponse
from products.models import Product


# Create your views here.
def index(request):
    """ Index page view """
    # return HttpResponse('t')
    products_slider = Product.objects.all().order_by('id')[:4]
    products_latest = Product.objects.all()

    context = {
        'products_slider': products_slider,
        'products_latest': products_latest,
    }
    return render(request, 'home/index.html', context)
