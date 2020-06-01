# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-30 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_catagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='catagory',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Plants', 'Plants'), ('Seeds', 'Seeds'), ('Equiptment', 'Equiptment'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]
