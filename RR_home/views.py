from django.shortcuts import render, HttpResponse, get_object_or_404
from products.models import Product, Images, Category
from random import choice


# Create your views here.
def index(request):
    """ Index page view """

    new_editions = Product.objects.filter(new_edition=True)
    categories = Category.objects.all().order_by('id')[:5]

    # product slider for new trends
    products_slider = Product.objects.all().order_by('id')[:40]
    products_latest = Product.objects.all().order_by('id')[:5]

    # Adding product ids to list to use for
    # displaying each product on home page template.
    category_ids = []
    for category in categories:
        category_ids.append(category.id)
    category_1 = get_object_or_404(Category, id=13)
    category_2 = get_object_or_404(Category, id=27)
    category_3 = get_object_or_404(Category, id=4)


    # Getting random id to display random products on home page with its
    # images getting them from images model
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
        'category_1': category_1,
        'category_2': category_2,
        'category_3': category_3,
        }

    return render(request, 'home/index.html', context)
