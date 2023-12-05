from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d', **NULLABLE, verbose_name='Фотография')
    date_birth = models.DateTimeField(**NULLABLE, verbose_name='Дата рождения')
