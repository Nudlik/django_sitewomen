from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about),
    path('women/cat/', views.catalog),
    path('', views.index),
    path('cats/', views.categories),
]
