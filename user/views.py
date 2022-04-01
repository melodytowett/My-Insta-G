from django.shortcuts import render
from .models import Image
# Create your views here.

def my_page(request):
    images = Image.objects.all()
    ctx = {'images':images}
    pages = Image.my_pages(images)
    return render(request,'index.html',ctx)
