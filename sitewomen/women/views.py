from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView

from .forms import AddPostForm, UploadImageForm, ContactFrom
from .models import Women
from .utils import DataMixin


class WomenHomeView(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    cat_selected = 0

    def get_queryset(self):
        return Women.published.all().select_related('cat')


def handle_uploaded_file(f):
    with open(f'uploads/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required
def about(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['image'])
    else:
        form = UploadImageForm()

    data = {
        'title': 'О сайте',
        'form': form,
    }
    return render(request, 'women/about.html', context=data)


class ShowPostView(DataMixin, DetailView):
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    title_page = 'Добавление статьи'
    permission_required = 'women.add_women'

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        return super().form_valid(form)


class UpdatePageView(PermissionRequiredMixin, DataMixin, UpdateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    success_url = reverse_lazy('women:home')
    title_page = 'Редактирование статьи'
    permission_required = 'women.change_women'

    def get_object(self, *args, **kwargs):
        post_slug = self.kwargs.get('post_slug')
        return get_object_or_404(Women, slug=post_slug)


class ContactFromView(LoginRequiredMixin, DataMixin, FormView):
    form_class = ContactFrom
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')
    title_page = 'Обратная связь'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Авторизация')


class WomenCategoryView(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,
                                      title=f'Категория - {cat.name}',
                                      cat_selected=cat.pk
                                      )


class WomenTagView(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['posts'][0].tags.all()[0]
        return self.get_mixin_context(context, title=f'Тег - {tag.tag}')
