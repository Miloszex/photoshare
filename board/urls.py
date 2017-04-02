from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'post-image/', views.post_image, name='post'),

]

