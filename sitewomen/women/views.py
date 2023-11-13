from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request: HttpRequest) -> HttpResponse:
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': [i for i in data_db if i['is_published']],
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request: HttpRequest, post_id: int) -> HttpResponse:
    return HttpResponse(f'Отображение статьи с id: {post_id}')


def add_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Добавление статьи')


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Обратная связь')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Авторизация')


def show_category(request: HttpRequest, cat_id: int) -> HttpResponse:
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': [i for i in data_db if i['is_published']],
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)
