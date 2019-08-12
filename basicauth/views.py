from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForms, EditProfileForms, EditPassForms
from .models import CustomUser

def home(request):
    count = CustomUser.objects.count()
    users = CustomUser.objects.all()
    context = {'users': users, 'count': count}
    return render(request, 'basicauth/home.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been Logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error Logging in!'))
            return redirect('login')
    else:
        return render(request, 'basicauth/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been Logged out!'))
    return redirect('home')

def reg_user(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have Registered!'))
            return redirect('home')

    else:
        form = SignUpForms()

    context = {'form': form}
    return render(request, 'basicauth/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForms(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have Edited your Profile!'))
            return redirect('home')

    else:
        form = EditProfileForms(instance=request.user)

    context = {'form': form}
    return render(request, 'basicauth/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = EditPassForms(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have Edited your Password!'))
            return redirect('home')

    else:
        form = EditPassForms(user=request.user)

    context = {'form': form}
    return render(request, 'basicauth/change_password.html', context)

