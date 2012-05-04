from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from archive.views import SeriesView



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'television.views.home', name='home'),
    # url(r'^television/', include('television.foo.urls')),
    #(r'^series/$', SeriesView.as_view()),
    (r'^series/(?P<series_slug>[-\w]+)', SeriesView.as_view()),
    #url(r'^series/(?P<series_slug>[-\w]+)', 'archive.views.series_detail'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))