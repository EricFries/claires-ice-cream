# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream_ordering', '0002_auto_20150516_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='image_url',
            field=models.CharField(max_length=200, default='d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icecream',
            name='image_url',
            field=models.CharField(max_length=200, default='d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topping',
            name='image_url',
            field=models.CharField(max_length=200, default='d'),
            preserve_default=False,
        ),
    ]
