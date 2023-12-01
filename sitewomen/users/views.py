from django.contrib.auth.views import LoginView

from users.forms import UserLoginForm


class LoginUserView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Авторизация',
    }
