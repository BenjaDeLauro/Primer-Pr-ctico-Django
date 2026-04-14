from django.contrib import admin
from django.urls import path
from core.views import home
from blog.views import lista_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('posts/', lista_posts, name='posts'),
]