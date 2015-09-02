# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20150902_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagesize',
            name='name',
        ),
    ]
