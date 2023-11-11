from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('О сайте')


def catalog(request: HttpRequest) -> HttpResponse:
    return HttpResponse('catalog')


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Страница приложения women')


def categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Статитьи по категориям</h1>')
