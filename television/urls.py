from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from archive.views import SeriesView, SeasonView, EpisodeView, SeriesBrowseView



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^series/$', SeriesBrowseView.as_view(), name='series_browse'),
    url(r'^series/(?P<series_slug>[-\w]+)/$', SeriesView.as_view(), name='series_detail'),
    url(r'^series/(?P<series_slug>[-\w]+)/season-(?P<season_num>\d+)/$', SeasonView.as_view(), name='season_detail'),
    url(r'^series/(?P<series_slug>[-\w]+)/season-(?P<season_num>\d+)/(?P<episode_slug>[-\w]+)/$', EpisodeView.as_view(), name='episode_detail'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))