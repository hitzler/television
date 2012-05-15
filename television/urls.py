from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from archive.views import SeriesView, SeasonView, EpisodeView



admin.autodiscover()

urlpatterns = patterns('',
    (r'^series/(?P<series_slug>[-\w]+)/$', SeriesView.as_view()),
    (r'^series/(?P<series_slug>[-\w]+)/(?P<season>[-\w]+)/$', SeasonView.as_view()),
    (r'^series/(?P<series_slug>[-\w]+)/(?P<season>[-\w]+)/(?P<episode_slug>[-\w]+)/$', EpisodeView.as_view()),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))