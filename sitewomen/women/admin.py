from django.contrib import admin, messages

from women.models import Women, Category, TagPost, Husband


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_create', 'is_published', 'brief_info', 'count_tags']
    list_display_links = ['title']
    ordering = ['-time_create', 'title']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    list_per_page = 10
    actions = ['set_published', 'set_draft']

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов'

    @admin.display(description='Количество тегов')
    def count_tags(self, women: Women):
        return len(women.tags.all())

    @admin.action(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей', messages.SUCCESS)

    @admin.action(description='В черновик')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'slug']
    list_display_links = ['id', 'tag']
    search_fields = ['tag']
    list_per_page = 10


@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'married']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10
