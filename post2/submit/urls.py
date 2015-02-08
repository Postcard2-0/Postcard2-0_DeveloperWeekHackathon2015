# AEttinger 7.2.15 - file created. This is for represntation of URLs in Django.
from django.conf.urls import patterns, url
from submit import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
)