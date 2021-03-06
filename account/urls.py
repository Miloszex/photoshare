"""photoshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index/$', views.index, name='index'),
    url(r'register/', views.register, name='register'),
    url(r'login/', views.login, name='login'),
    url(r'profile/', views.profile, name='profile'),
    url(r'delete_avatar/', views.delete_avatar, name='delete_avatar'),
    url(r'logout/', views.logout_user, name='logout'),
    url(r'search_for_user/', views.search_for_user, name='search_for_user'),
   # url(r'add/(?P<username>[A-Z a-z]+)/', views.add_user, name='add_user')
]
