from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.forms import UserLoginForm


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None and user.is_active:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('users:login')
