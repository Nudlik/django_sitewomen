from django.db import models
from django.urls import reverse


NULLABLE = {'null': True, 'blank': True}


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT, verbose_name='Опубликовано')
    cat = models.ForeignKey(to='Category', on_delete=models.PROTECT, verbose_name='Категория')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return f'({self.pk}){self.title}'

    class Meta:
        verbose_name = 'Женщина'
        verbose_name_plural = 'Женщины'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self) -> str:
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.name
