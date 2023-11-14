from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.title} ({self.content[:20]}...)'

    class Meta:
        verbose_name = 'Женщина'
        verbose_name_plural = 'Женщины'
