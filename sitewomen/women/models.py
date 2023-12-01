import transliterate
from django.contrib.auth import get_user_model
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
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT,
                                       verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, **NULLABLE, verbose_name='Фото')

    cat = models.ForeignKey(to='Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(to='TagPost', blank=True, related_name='women', verbose_name='Теги')
    husband = models.OneToOneField(to='Husband',
                                   on_delete=models.SET_NULL,
                                   **NULLABLE,
                                   related_name='married',
                                   verbose_name='Супруг')
    author = models.ForeignKey(get_user_model(),
                               **NULLABLE,
                               on_delete=models.SET_NULL,
                               default=None,
                               related_name='post_author')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = transliterate.slugify(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True, verbose_name='Тег')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.tag

    def get_absolute_url(self) -> str:
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    age = models.IntegerField(**NULLABLE, verbose_name='Возраст')

    class Meta:
        verbose_name = 'Супруг'
        verbose_name_plural = 'Супруги'

    def __str__(self):
        return self.name
