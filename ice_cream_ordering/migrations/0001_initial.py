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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('option', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('flavor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=75)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=30)),
                ('date', models.DateTimeField(verbose_name='date ordered')),
                ('container', models.ForeignKey(to='ice_cream_ordering.Container')),
                ('flavors', models.ManyToManyField(to='ice_cream_ordering.IceCream')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('variety', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='topping',
            field=models.ForeignKey(to='ice_cream_ordering.Topping'),
        ),
    ]
