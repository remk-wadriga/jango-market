# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import market.ext.File


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20150901_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSize',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('type', models.IntegerField(default=2, choices=[(0, 'Миниатюра'), (1, 'Основное изображение'), (2, 'Обычное изображение')])),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='is_miniature',
        ),
        migrations.RemoveField(
            model_name='image',
            name='is_primary',
        ),
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ImageField(max_length=400, storage=market.ext.File.Storage(), upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
