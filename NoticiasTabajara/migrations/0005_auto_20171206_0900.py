# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoticiasTabajara', '0004_auto_20171110_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='active_status',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='noticia',
            name='comentarios',
            field=models.ManyToManyField(to='NoticiasTabajara.Comentario'),
        ),
    ]
