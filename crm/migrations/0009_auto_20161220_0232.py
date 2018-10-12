# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-20 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20161219_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstlayermenu',
            name='url_type',
            field=models.SmallIntegerField(choices=[(0, 'related_name'), (1, 'absolute_url')], default=0),
        ),
        migrations.AlterUniqueTogether(
            name='firstlayermenu',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='firstlayermenu',
            name='arg1',
        ),
        migrations.RemoveField(
            model_name='firstlayermenu',
            name='arg2',
        ),
        migrations.RemoveField(
            model_name='firstlayermenu',
            name='arg3',
        ),
    ]
