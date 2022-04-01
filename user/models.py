

from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('image',blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

class Image(models.Model):
    image_name = models.CharField(max_length=40)
    image = CloudinaryField ('image')
    image_caption = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile ,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()


    @classmethod
    def my_page(cls,name):
        page = cls.objects.filter(image_name__in=name)
        return page