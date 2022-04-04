from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.my_page,name='my_page'),
    path('profile/',views.my_profile,name='profile'),
    path('accounts/register/',views.register_user,name="register"),
    path('accounts/login/',views.login_user,name='login'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('search/',views.search_results,name='search_user'),
    path('new_post/',views.new_post,name='new-post')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)