# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream_ordering', '0002_auto_20150516_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('flavor', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='flavor',
        ),
        migrations.AddField(
            model_name='icecream',
            name='order',
            field=models.ForeignKey(to='ice_cream_ordering.Order'),
        ),
    ]
