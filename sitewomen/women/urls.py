from django.urls import path, register_converter

from . import converter
from . import views


register_converter(converter.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('about/', views.about),
    path('women/cat/', views.catalog),
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    path('archive/<year4:year>/', views.archive),
    path('post/', views.post_detail),
    path('posts/<int:year>/', views.posts_list),
]
