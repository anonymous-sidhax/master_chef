from django.urls import path
from .views import Home, UploadImage, AboutUs

urlpatterns = [
    path('', Home, name="HomePage"),
    path('uploadImage/', UploadImage, name="UploadImage"),
    path('AboutUs/', AboutUs, name="AboutUs"),
]