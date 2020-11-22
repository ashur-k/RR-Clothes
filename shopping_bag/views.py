from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from products.models import Product, Variants
from django.contrib import messages


# Create your views here.
def view_bag(request):
    # print(request.session.get('bag')

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    variant = get_object_or_404(Variants, pk=item_id)

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'{bag[item_id]} {variant.size} {variant.color} {variant.title}s are added to your bag.')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {variant.size} {variant.color} {variant.title}   to your bag.')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):

    variant = get_object_or_404(Variants, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'{quantity} {variant.title} in your bag is ')
    else:
        bag.pop(item_id)
        messages.success(request, f'{variant.title} successfully removed from your bag.')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    try:
        variant = get_object_or_404(Variants, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'{variant.title} removed from bag.')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect(reverse('view_bag'))
