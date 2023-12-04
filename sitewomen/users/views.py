from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserLoginForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


class LoginUserView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Авторизация',
    }


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {
        'title': 'Регистрация',
    }


class ProfileUserView(LoginRequiredMixin, UpdateView):
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users:password_change_done')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'
    extra_context = {
        'title': 'Ваш пароль был успешно изменен!',
        'button': 'Вернуться в профиль',
    }


class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    extra_context = {
        'title': 'Восстановление пароля',
        'button': 'Сбросить по E-mail',
    }


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
    extra_context = {
        'title': 'Сброс пароля',
    }


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')
    extra_context = {
        'title': 'Новый пароль',
        'button': 'Сохранить',
    }


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
    extra_context = {
        'title': 'Восстановление пароля завершено',
    }
