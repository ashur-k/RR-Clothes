from django.shortcuts import render, HttpResponse, get_object_or_404
from products.models import Product, Images
from random import choice


# Create your views here.
def index(request):
    """ Index page view """
    # return HttpResponse('t')
    products_slider = Product.objects.all().order_by('id')[:4]
    products_latest = Product.objects.all().order_by('id')[:5]
    product_ids = []
    for product in products_latest:    
        product_ids.append(product.id)
    
  
    latest_product_1 = get_object_or_404(Product, id=product_ids[0])
    latest_product_2 = get_object_or_404(Product, id=product_ids[1])
    latest_product_3 = get_object_or_404(Product, id=product_ids[2])
    latest_product_4 = get_object_or_404(Product, id=product_ids[3])
    latest_product_5 = get_object_or_404(Product, id=product_ids[4])
   

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
        'latest_product_1': latest_product_1,
        'latest_product_2': latest_product_2,
        'latest_product_3': latest_product_3,
        'latest_product_4': latest_product_4,
        'latest_product_5': latest_product_5,
    }
    return render(request, 'home/index.html', context)
