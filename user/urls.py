from django.conf import settings
from django.urls import path,include,re_path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.my_page,name='my_page'),
    path('profile/',views.my_profile,name='profile'),
    path('accounts/register/',views.register_user,name="register"),
    re_path(r'login/',views.login_user,name='login'),
    path("logout", views.logout_request, name= "logout"),
    # path('accounts/', include('django.contrib.auth.urls')),
    re_path('comment',views.comment_post,name='comment'),
    path('search/',views.search_results,name='search_user'),
    path('new_post/',views.new_post,name='new-post')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)