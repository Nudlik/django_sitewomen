from django import forms
from .models import Category, Husband, TagPost


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    slug = forms.SlugField(max_length=255, label='Слаг')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Содержимое')
    is_published = forms.BooleanField(label='Опубликовано', required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Супруги')
    tags = forms.ModelMultipleChoiceField(queryset=TagPost.objects.all(), required=False, label='Теги')

