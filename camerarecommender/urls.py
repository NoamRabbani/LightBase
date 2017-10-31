from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /camerarecommender/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.question, name='question'),
]
