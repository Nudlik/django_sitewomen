from django import template
from django.db.models import Count

from women.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags(cat_selected=None):
    tags = TagPost.objects.annotate(total=Count('women')).filter(total__gt=0)
    return {'tags': tags, 'cat_selected': cat_selected}
