from django.conf.urls import patterns, url

from suber import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)