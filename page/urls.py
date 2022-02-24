from django.urls import path
from .views import carousel_create, index



urlpatterns = [
    path('', index, name='index'),
    path('carousel_create/', carousel_create, name='carousel_create'), 
] 