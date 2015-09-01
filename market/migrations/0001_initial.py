# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('parent', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('path', models.ImageField(max_length=400, upload_to='market/static/img')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('is_miniature', models.BooleanField()),
                ('is_primary', models.BooleanField()),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('cost', models.FloatField()),
                ('rate', models.IntegerField(blank=True)),
                ('count', models.FloatField()),
                ('min_count', models.FloatField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.IntegerField(default=1, choices=[(0, 'Неактивен'), (1, 'Активен'), (2, 'Удалён')])),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(blank=True)),
                ('categories', models.ManyToManyField(to='market.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('value', models.CharField(max_length=255)),
                ('product', models.ForeignKey(to='market.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('cost_coefficient', models.FloatField()),
                ('categories', models.ManyToManyField(to='market.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(to='market.Country')),
            ],
        ),
        migrations.AddField(
            model_name='productproperty',
            name='property',
            field=models.ForeignKey(to='market.Property'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(to='market.Unit'),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(to='market.Vendor'),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(to='market.Product'),
        ),
    ]
