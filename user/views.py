
from django.shortcuts import render,redirect

import user
from .models import Image
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
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

