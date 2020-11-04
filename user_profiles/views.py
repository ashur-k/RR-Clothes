from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.models import User


# Create your views here.
def user_profiles(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'user_profiles/user_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        'user': user
    }
    return render(request, template, context)
