# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream_ordering', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icecream',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='flavor',
            field=models.CharField(max_length=30, default='chocolate'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='IceCream',
        ),
    ]
