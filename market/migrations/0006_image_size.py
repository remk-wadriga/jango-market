# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_remove_imagesize_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='size',
            field=models.ForeignKey(to='market.ImageSize', default=1),
            preserve_default=False,
        ),
    ]
