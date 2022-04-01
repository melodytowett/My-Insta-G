from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from.import views

urlpattern = [
    path('',views.my_page,name='my_page')
]
if settings.DEBUG:
    urlpattern+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)