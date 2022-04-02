
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.my_page,name='my_page'),
    path('register',views.register_user,name='register'),
    path('login',views.login_user,name="login"),
    # path('accounts/', include('django_registration.backends.one_step.urls')),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)