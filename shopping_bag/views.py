from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from products.models import Product, Variants


# Create your views here.
def view_bag(request):
    # print(request.session.get('bag')

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

    return redirect(redirect_url)


def adjust_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):

    bag = request.session.get('bag', {})

    bag.pop(item_id)

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))
