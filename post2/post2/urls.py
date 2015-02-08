from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'post2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # AEttinger 7.2.15 - added to point to the submit URL.
    url(r'^submit/',include('submit.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
