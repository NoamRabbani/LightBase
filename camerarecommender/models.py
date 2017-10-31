# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Camera(models.Model):
    brand = models.CharField(max_length=200,null=True)
    resolution = models.IntegerField(default=0)

class Filter(models.Model):
    session_id = models.CharField(max_length=200,null=True)
    json_brand = models.CharField(max_length=200,null=True)
    json_resolution = models.CharField(max_length=200,null=True)

class Question(models.Model):
    text = models.CharField(max_length=200,null=True)
    tag = models.CharField(max_length=200,null=True)
    json_options = models.CharField(max_length=200,null=True)
