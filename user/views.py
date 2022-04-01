from django.shortcuts import render
from models import Image
# Create your views here.

def my_page(request):
    page = Image.objects.all()
    return render(request,'index.html',{"page":page})
