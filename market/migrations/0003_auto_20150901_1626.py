# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20150901_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
