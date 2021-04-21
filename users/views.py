from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegisterFrom,CreateProfileForm
from .models import *

def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('create_profile')
    else:
        form = UserRegisterFrom()
    return render(request, 'register.html', {'form':form})


def create_profile(request):
    user = request.user
    if Profile.objects.filter(user=user).exists():
        return redirect('profile')
    else:
        pass
    if request.method == 'POST':
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.info(request, "Your profile is saved successfully")
            return redirect('profile')
    else:
        form = CreateProfileForm()
    return render(request, 'create_profile.html',locals())


def profile(request):
    user = request.user
    if Profile.objects.filter(user=user).exists():
        profile = Profile.objects.get(user=user)
    else:
        return redirect('create_profile')
    return render(request, 'profile.html',locals())

