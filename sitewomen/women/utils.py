menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


class DataMixin:
    title_page = None
    cat_selected = None
    extra_context = {'menu': menu}

    def __init__(self):
        # self_items = vars(self.__class__.__mro__[0]).items()
        # for attr_name, attr_value in self_items:
        #     if not attr_name.startswith('__') and not callable(attr_value) and attr_name != 'extra_context':
        #         print(f'{attr_name} = {attr_value}')
        #         self.extra_context[attr_name] = attr_value

        # if 'menu' not in self.extra_context:
        #     self.extra_context['menu'] = menu

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

        if self.title_page is not None:
            self.extra_context['title_page'] = self.title_page

    def get_mixin_context(self, context: dict, **kwargs) -> dict:
        context['menu'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context
