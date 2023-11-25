from django import forms
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, TagPost


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- ')
    code = 'russian'

    def __init__(self, msg=None):
        self.msg = msg if msg else 'Должны быть только: русские символы, цифры, дефис или пробел'

    def __call__(self, word, *args, **kwargs):
        if not all(char in self.ALLOWED_CHARS for char in word):
            raise forms.ValidationError(self.msg, code=self.code)


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255,
                            label='Заголовок',
                            validators=[
                                RussianValidator(),
                            ],
                            )
    slug = forms.SlugField(max_length=255, label='Слаг')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'Содержимое статьи'}),
                              required=False, label='Содержимое')
    is_published = forms.BooleanField(label='Опубликовано', initial=True, required=False)

    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Не замужем',
                                     required=False, label='Супруги')
    tags = forms.ModelMultipleChoiceField(queryset=TagPost.objects.all(), required=False, label='Теги')
