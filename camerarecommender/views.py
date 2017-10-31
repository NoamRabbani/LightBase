# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'camerarecommender/index.html')

def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    options = question.json_options
    print(options)
    context = { "text" : question.text , "tag" : question.tag , "json_options" : question.json_options}
    return render(request, 'camerarecommender/question.html', context)
