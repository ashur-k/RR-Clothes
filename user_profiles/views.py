from django.shortcuts import render, get_object_or_404
from .models import UserProfile


# Create your views here.
def user_profiles(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'user_profiles/user_profile.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)
