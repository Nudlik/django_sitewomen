from django import forms
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, TagPost, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- ')
    code = 'russian'

    def __init__(self, msg=None):
        self.msg = msg if msg else 'Должны быть только: русские символы, цифры, дефис или пробел'

    def __call__(self, word, *args, **kwargs):
        if not all(char in self.ALLOWED_CHARS for char in word):
            raise forms.ValidationError(self.msg, code=self.code)


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Не замужем',
                                     required=False, label='Супруги')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'Содержимое статьи'}),
            # 'tags': forms.CheckboxSelectMultiple(attrs={'class': 'horizontal'}),
        }
        labels = {
            'slug': 'URL',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- ')
        if not all(char in ALLOWED_CHARS for char in title):
            raise forms.ValidationError('Должны быть только: русские символы, цифры, дефис или пробел')
        return title
