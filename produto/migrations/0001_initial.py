# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidade', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
