from django.shortcuts import render, HttpResponse, get_object_or_404
from products.models import Product, Images, Category, Variants
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
    category_1 = get_object_or_404(Category, id=5)
    category_2 = get_object_or_404(Category, id=27)
    category_3 = get_object_or_404(Category, id=15)
    category_4 = get_object_or_404(Category, id=9)
    category_5 = get_object_or_404(Category, id=6)


    # Getting random id to display random products on home page with its
    # images getting them from images model
    random_pks = Product.objects.values_list('pk', flat=True)
    random_pk = choice(random_pks)
    print(random_pk)
    random_product = Product.objects.get(pk=49)
    product_id = random_product.id
    print(product_id)
    images = Images.objects.filter(product_id=49)
    variants = Variants.objects.filter(product_id=49)

    context = {
        'products_slider': products_slider,
        'products_latest': products_latest,
        'product': random_product,
        'images': images,
        'category_1': category_1,
        'category_2': category_2,
        'category_3': category_3,
        'category_4': category_4,
        'category_5': category_5,
        'variants': variants,
        }

    return render(request, 'RR_home/index.html', context)
