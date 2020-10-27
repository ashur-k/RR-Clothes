from django.shortcuts import render, HttpResponse


# Create your views here.
def view_bag(request):
    return HttpResponse("Shopping bag working")
