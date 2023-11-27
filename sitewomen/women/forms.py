from django import forms

from .models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Не замужем',
                                     required=False, label='Супруги')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags']
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


class UploadImageForm(forms.Form):
    image = forms.ImageField()
