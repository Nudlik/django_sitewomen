menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
]


class DataMixin:
    title_page = None
    cat_selected = None
    extra_context = {}
    paginate_by = 5

    def __init__(self):

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

        if self.title_page is not None:
            self.extra_context['title'] = self.title_page

    def get_mixin_context(self, context: dict, **kwargs) -> dict:
        context['menu'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context
