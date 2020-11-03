from django.shortcuts import render


# Create your views here.
def user_profiles(request):
    template = 'user_profiles/user_profile.html'
    context = {

    }
    return render(request, template, context)
