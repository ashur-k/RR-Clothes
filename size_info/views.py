from django.shortcuts import render, HttpResponse


# Create your views here.
def girl_size_info(request):
    return render(request, 'size_info/girl_size_info.html')


def boy_size_info(request):
    return render(request, 'size_info/boy_size_info.html')


def women_size_info(request):
    return render(request, 'size_info/women_size_info.html')


def men_size_info(request):
    return render(request, 'size_info/men_size_info.html')
