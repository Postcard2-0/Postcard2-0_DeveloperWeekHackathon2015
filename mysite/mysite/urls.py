from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^suber/', include('suber.urls', namespace="suber")),
    url(r'^submit_new/', include('submit_new.urls')),
    url(r'^admin/', include(admin.site.urls)),
)