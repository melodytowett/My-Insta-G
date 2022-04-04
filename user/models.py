
from email.mime import image
from xml.etree.ElementTree import Comment
from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('profile')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

class Image(models.Model):
    image_name = models.CharField(max_length=40)
    image = CloudinaryField ('image')
    image_caption = models.CharField(max_length=200)
    user = models.ForeignKey(User ,on_delete=models.CASCADE,null=True)
    likes = models.IntegerField(default=0)
    comments = HTMLField()

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    
    @classmethod
    def my_pages(cls,name):
        page = cls.objects.filter(image_name__in=name)
        return page
    @classmethod
    def search_by_name(cls,search_term):
        names = cls.objects.filter(image_name__icontains = search_term)
        return names
class Follow(models.Model):
    followers =  models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='following')
    followed = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='followers')

    def __str__(self):
        return self.followers
class Comments(models.Model):
    comment  = models.TextField()
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comment_post')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.comment

@classmethod
def show_coments(cls,image_id):
    comments = cls.objects.filter(image_id=image_id)
    return comments


