from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from women.models import Women, Category, TagPost, Husband


class MariedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        if self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ['title', 'cat', 'show_photo', 'time_create', 'is_published', 'brief_info', 'count_tags']
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ['title']
    ordering = ['-time_create', 'title']
    search_fields = ['title', 'cat__name']
    list_editable = ['is_published']
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    list_filter = ['is_published', MariedFilter, 'cat__name']
    fields = ['title', 'slug', 'cat', 'content', 'photo', 'show_photo', 'tags', 'is_published']
    readonly_fields = ['show_photo']
    filter_horizontal = ['tags']
    save_on_top = True

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов'

    @admin.display(description='Количество тегов')
    def count_tags(self, women: Women):
        return len(women.tags.all())

    @admin.display(description='Предпросмотр фотографии')
    def show_photo(self, women: Women):
        if women.photo:
            return mark_safe(f'<img src="{women.photo.url}" width="50"')
        return 'Фото отсутствует'

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
