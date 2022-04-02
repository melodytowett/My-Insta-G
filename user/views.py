
from django.http import request
from django.shortcuts import render,redirect

import user
from .models import Image
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def my_page(request):
    images = Image.objects.all()
    ctx = {'images':images}
    pages = Image.my_pages(images)
    return render(request,'index.html',ctx) 

def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration successful.")
            return redirect("my_page")
        messages.error(request,"Invalid credentials.")
    form=NewUserForm()
    return render(request,'registration/register.html',context={"register_form":form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                # messages.info(request,)
                return redirect("user:my_page")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"invalid username or password.")
    form = AuthenticationForm()
    return render(request,'registration/login.html',context={"login_form":form})


