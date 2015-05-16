# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('option', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('flavor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=75)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=30)),
                ('date', models.DateTimeField(verbose_name='date ordered')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('variety', models.CharField(max_length=30)),
                ('order', models.ForeignKey(to='ice_cream_ordering.Order')),
            ],
        ),
        migrations.AddField(
            model_name='icecream',
            name='order',
            field=models.ForeignKey(to='ice_cream_ordering.Order'),
        ),
        migrations.AddField(
            model_name='container',
            name='order',
            field=models.ForeignKey(to='ice_cream_ordering.Order'),
        ),
    ]
