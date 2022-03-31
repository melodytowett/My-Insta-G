from distutils.command.upload import upload
from operator import mod
import profile
from pyexpat import model
from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to = '/article',blank =True)
    name = models.CharField(max_length=40)
    caption = models.CharField(max_length=50)
    profile = models.ForeignKey()
    likes = models.CharField()
    comments = models