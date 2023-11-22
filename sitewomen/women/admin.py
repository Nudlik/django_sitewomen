from django.contrib import admin

from women.models import Women


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    pass
