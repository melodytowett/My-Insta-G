
import profile
from django.http import request
from django.shortcuts import render,redirect
from django .contrib.auth.decorators import login_required
from .forms import NewPostForm,ProfileForm
from .models import Image, Profile
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration successfull.")
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

@login_required(login_url='/accounts/login/')
def my_page(request):
    images = Image.objects.all()
    ctx = {'images':images}
    pages = Image.my_pages(images)
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
            return redirect("my_page")
         
    else:
        form=NewPostForm()
    return render(request,'index.html',ctx)

@login_required(login_url='/accounts/login/')
def my_profile(request):
    profiles = Profile.objects.all()
    ctx = {'profiles':profiles}
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect("my_page")
    else:
        form=ProfileForm()
    return render(request,'profile.html',{"profile_form":form})


    



