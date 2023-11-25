from django import forms
from .models import Category, Husband, TagPost


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    slug = forms.SlugField(max_length=255, label='Слаг')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'Содержимое статьи'}),
                              required=False, label='Содержимое')
    is_published = forms.BooleanField(label='Опубликовано', initial=True, required=False)

    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Не замужем',
                                     required=False, label='Супруги')
    tags = forms.ModelMultipleChoiceField(queryset=TagPost.objects.all(), required=False, label='Теги')
