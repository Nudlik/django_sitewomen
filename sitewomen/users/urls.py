from django.urls import path

from . import views
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
