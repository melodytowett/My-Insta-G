from distutils.command.upload import upload

from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='',blank=True)
    bio = models.CharField

class Image(models.Model):
    image = CloudinaryField ('image')
    image_name = models.CharField(max_length=40)
    image_caption = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile ,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models

