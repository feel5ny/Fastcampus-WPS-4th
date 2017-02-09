# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20170209_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_set', to='person.Person', verbose_name='담당 강사'),
        ),
    ]
