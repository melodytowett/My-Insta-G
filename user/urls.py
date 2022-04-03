
from re import search
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.my_page,name='my_page'),
    path('profile/',views.my_profile,name='profile'),
    path('search/',views.search_results,name='search_user')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)