from django.conf.urls import patterns, url

from suber import views

urlpatterns = patterns('',
    url(r'^$', views.index2, name='index2'),
)