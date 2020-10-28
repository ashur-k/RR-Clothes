from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from products.models import Product, Variants


# Create your views here.
def view_bag(request):
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id, variant_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if variant_id in list(bag.keys()):
        bag[variant_id] += quantity
    else:
        bag[variant_id] = quantity

    request.session['bag'] = bag
    print(variant_id)

    return redirect(redirect_url)
