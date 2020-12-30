from django.shortcuts import render, HttpResponse


# Create your views here.
def size_info(request, product_id):
    template = 'size_info/size_info.html'
    context = {
        'product_id': product_id,
    }
    return render(request, template, context)
