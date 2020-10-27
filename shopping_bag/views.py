from django.shortcuts import render, HttpResponse


# Create your views here.
def view_bag(request):
    return render(request, 'shopping_bag/shopping_bag.html')
