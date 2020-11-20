from django.shortcuts import render, HttpResponse
from products.models import Product, Images
from random import choice


# Create your views here.
def index(request):
    """ Index page view """
    # return HttpResponse('t')
    products_slider = Product.objects.all().order_by('id')[:4]
    products_latest = Product.objects.all().order_by('id')[:5]
    #new_product = Product.objects.get(id)
    #product_id = products_latest
    random_pks = Product.objects.values_list('pk', flat=True)    
    random_pk = choice(random_pks)    
    random_product = Product.objects.get(pk=random_pk)
    product_id = random_product.id
    images = Images.objects.filter(product_id=product_id)

    context = {
        'products_slider': products_slider,
        'products_latest': products_latest,
        'product': random_product,
        'images': images,
    }
    return render(request, 'home/index.html', context)
