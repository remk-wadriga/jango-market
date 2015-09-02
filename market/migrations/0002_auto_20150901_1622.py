# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import market.ext.File


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ImageField(upload_to='market/media/products', storage=market.ext.File.Storage, max_length=400),
        ),
    ]
