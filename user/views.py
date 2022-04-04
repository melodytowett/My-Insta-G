
from django.http import request
from django.shortcuts import render,redirect
from django .contrib.auth.decorators import login_required
from .forms import CommentForm, NewPostForm,ProfileForm
from .models import Image, Profile
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
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
            return redirect(my_page)
        messages.error(request,"Invalid credentials.")
        # return redirect('/login')

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
                messages.info(request,f"you are now loged in as {username}")
                return redirect("my_page")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"invalid username or password.")
    form = AuthenticationForm()
    return render(request,'registration/login.html',context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("my_page")

@login_required(login_url='login/')
def my_page(request):
    images = Image.objects.all()
    ctx = {'images':images}
    pages = Image.my_pages(images)
    return render(request,'index.html',ctx)

@login_required(login_url='login/')
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

@login_required(login_url='accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        pform = NewPostForm(request.POST,request.FILES)
        if pform.is_valid():
            post = pform.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('my_page')
    else:
        pform = NewPostForm()
    return render(request,'pages/my-page.html',{"pform":pform})

@login_required(login_url='accounts/login/')
def comment_post(request):
    current_user = request.user
    if request.method == 'POST':
        coform = CommentForm(request.POST,request.FILES)
        if coform.is_valid():
            comment = coform.save(commit=False)
            comment.user = current_user
            comment.save()
            return redirect('my_page')
    else:
        coform = CommentForm()
    return render(request,'pages/comment.html',{"coform":coform})
        

@login_required(login_url='accounts/login/')
def search_results(request):
    images = Image.objects.all()
    if 'name'in request.GET and request.GET['name']:
        search_term = request.GET.get("name")
        name_searched = Image.search_by_name(search_term)
        return render(request,'pages/search.html',{"names":name_searched,"images":images})
    else:
        message = "No related search"
        return render(request,'pages/search.html',{"message":message})
    



