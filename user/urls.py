
from re import search
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views
app_name = "user"

urlpatterns = [
    path('',views.my_page,name='my_page'),
    path('profile/',views.my_profile,name='profile'),
    path('register',views.register_user,name="register"),
    path('login',views.login_user,name='login'),
    path('search/',views.search_results,name='search_user'),
    path('new_post/',views.new_post,name='new-post')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)