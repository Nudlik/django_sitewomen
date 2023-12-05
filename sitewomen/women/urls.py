from django.urls import path, register_converter

from . import converter
from . import views

register_converter(converter.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.WomenHomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>/', views.ShowPostView.as_view(), name='post'),
    path('addpage/', views.AddPageView.as_view(), name='add_page'),
    path('edit/<slug:post_slug>/', views.UpdatePageView.as_view(), name='edit_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<slug:cat_slug>/', views.WomenCategoryView.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.WomenTagView.as_view(), name='tag'),
]
