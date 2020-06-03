# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-03 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200530_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('plants', 'plants'), ('seeds', 'seeds'), ('equiptment', 'equiptment'), ('other', 'other')], default='other', max_length=20),
        ),
    ]
