# Generated by Django 4.2.7 on 2023-11-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0009_alter_category_options_alter_husband_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]