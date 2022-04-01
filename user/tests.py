
from django.test import TestCase
from .models import Image,Profile
# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.images = Image(image_name="Beach",image_caption="Beach in africa",likes=0,comments="amazing")
        self.images.save_image()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.images,Image))

    def test_save_page(self):
        self.images.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def tearDown(self):
        Image.objects.all().delete()

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(bio = "This is what you dont know about me")

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def tearDown(self):
        Profile.objects.all().delete()
        