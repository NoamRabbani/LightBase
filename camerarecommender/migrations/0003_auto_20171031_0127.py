# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camerarecommender', '0002_auto_20171031_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='SessionID',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='camera',
            name='Brand',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='JSONBrand',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='JSONResolution',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='questionchar',
            name='JSONOptions',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='questionchar',
            name='Tag',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='questionchar',
            name='Text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]