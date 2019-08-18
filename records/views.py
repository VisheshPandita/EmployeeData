from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from .forms import *

def homepage(request):
    return render(request,"homepage.html",{})

def data(request):
    data = User.objects.all()
    context = {
        'data': data,
    }
    return render(request,"records.html",context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save() 
            return redirect('data')
    else:
        form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {"form":form, "profile_form": profile_form,})
