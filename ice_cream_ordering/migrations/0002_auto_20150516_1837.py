# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream_ordering', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='flavors',
        ),
        migrations.RemoveField(
            model_name='order',
            name='topping',
        ),
        migrations.AddField(
            model_name='order',
            name='flavor',
            field=models.ForeignKey(to='ice_cream_ordering.IceCream', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='toppings',
            field=models.ManyToManyField(to='ice_cream_ordering.Topping'),
        ),
    ]
