from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'television.views.home', name='home'),
    # url(r'^television/', include('television.foo.urls')),
    url(r'^series/(?P<series_slug>[-\w]+)', 'archive.views.series_detail'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
