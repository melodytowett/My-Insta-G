from django.shortcuts import render
from .models import Image
# Create your views here.

def my_page(request):
    images = Image.objects.all()
    pages = Image.my_page(images)

    return render(request,'index.html',{"page":pages})
