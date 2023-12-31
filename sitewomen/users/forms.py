import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class MixinWidgets:

    class Meta:
        widgets = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        widgets = self.Meta.widgets
        if widgets:
            for field_name, widget in widgets.items():
                self.fields[field_name].widget = widget


class UserLoginForm(MixinWidgets, AuthenticationForm):
    username = forms.CharField(label='Логин/E-mail')
    password = forms.CharField(label='Пароль')

    class Meta:
        model = get_user_model()
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш логин'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ваш пароль'}),
        }


class RegisterUserForm(MixinWidgets, UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким E-mail уже существует')
        return email


class ProfileUserForm(MixinWidgets, forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин')
    email = forms.CharField(disabled=True, required=False, label='E-mail')

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'date_birth': 'Дата рождения',
        }
        this_year = datetime.date.today().year
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.SelectDateWidget(years=range(this_year - 100, this_year - 5),
                                                 attrs={'class': 'form-control'}),
        }


class UserPasswordChangeForm(MixinWidgets, PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль')
    new_password1 = forms.CharField(label='Новый пароль')
    new_password2 = forms.CharField(label='Подтверждение пароля')

    class Meta:
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
