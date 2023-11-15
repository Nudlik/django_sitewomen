from django.db import models
from django.urls import reverse


NULLABLE = {'null': True, 'blank': True}


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

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
