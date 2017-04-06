from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'post-image/', views.post_image, name='post'),
    url(r'my_photos/', views.showMyPhotos, name='show_my_photos'),

]

