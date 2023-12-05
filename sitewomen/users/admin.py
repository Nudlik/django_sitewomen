from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'email', 'show_group', 'first_name', 'last_name', 'is_staff']

    @admin.display(description='Группы')
    def show_group(self, obj):
        return ', '.join([group.name for group in obj.groups.all()])
