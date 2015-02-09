from django.conf.urls import patterns, url

from submit_new import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)