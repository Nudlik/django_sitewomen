# Generated by Django 4.2.7 on 2023-12-01 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('women', '0010_women_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='author',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_author', to=settings.AUTH_USER_MODEL),
        ),
    ]