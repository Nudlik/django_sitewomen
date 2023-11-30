from django import forms


class MixinWidgets:
    widgets = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.widgets:
            for field_name, widget in self.widgets.items():
                self.fields[field_name].widget = widget


class UserLoginForm(MixinWidgets, forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш логин'}),
        'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ваш пароль'}),
    }

