from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('О сайте')


def catalog(request: HttpRequest) -> HttpResponse:
    return HttpResponse('catalog')


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Страница приложения women')


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f'<h1>Статитьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request: HttpRequest, cat_slug: str) -> HttpResponse:
    return HttpResponse(f'<h1>Статья по slug</h1><p>slug: {cat_slug}</p>')


def archive(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')
