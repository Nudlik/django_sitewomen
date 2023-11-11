from django.urls import path, register_converter

from . import converter
from . import views


register_converter(converter.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('about/', views.about, name='about'),
    path('women/cat/', views.catalog, name='catalog'),
    path('', views.index, name='home'),
    path('cats/<int:cat_id>/', views.categories, name='categories'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='categories_by_slug'),
    path('archive/<year4:year>/', views.archive, name='archive'),
    path('post/', views.post_detail, name='post_'),
    path('posts/<int:year>/', views.posts_list, name='posts_list'),
]
