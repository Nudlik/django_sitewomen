from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from .forms import AddPostForm, UploadImageForm
from .models import Women, Category, TagPost

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


class WomenHomeView(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0,
    }

    def get_queryset(self):
        return Women.published.all().select_related('cat')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
        # context['title'] = 'Главная страница'
        # context['menu'] = menu
        # context['cat_selected'] = 0
        # return context


def handle_uploaded_file(f):
    with open(f'uploads/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['image'])
    else:
        form = UploadImageForm()

    data = {
        'title': 'О сайте',
        'menu': menu,
        'form': form,
    }
    return render(request, 'women/about.html', context=data)


def show_post(request: HttpRequest, post_slug: str) -> HttpResponse:
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 0,
    }

    return render(request, 'women/post.html', context=data)


class AddPageView(View):
    def get(self, request):
        form = AddPostForm()
        data = {
            'title': 'Добавление статьи',
            'menu': menu,
            'form': form,
        }
        return render(request, 'women/add_page.html', context=data)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        data = {
            'title': 'Добавление статьи',
            'menu': menu,
            'form': form,
        }
        return render(request, 'women/add_page.html', context=data)


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Обратная связь')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Авторизация')


class WomenCategoryView(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = f'Категория - {cat.name}'
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context


def show_tag_postlist(request: HttpRequest, tag_slug: str) -> HttpResponse:
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = Women.published.filter(tags__slug=tag.slug).select_related('cat')

    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)
