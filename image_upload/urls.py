# image_upload/urls.py

from django.urls import path
from .views import image_upload,image_list

urlpatterns = [
    path('', image_upload, name='image_upload'),
    path('list/', image_list, name='image_list'),
]
