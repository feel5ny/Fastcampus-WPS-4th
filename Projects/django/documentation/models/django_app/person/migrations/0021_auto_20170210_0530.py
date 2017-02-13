# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0020_article_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Article'),
        ),
    ]