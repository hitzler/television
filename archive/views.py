from archive.models import Series, Season, Episode
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class SeriesView(TemplateView):
    template_name = 'archive/series_detail.html'

    def get_context_data(self, **kwargs):
        series = get_object_or_404(Series, slug=kwargs['series_slug'])
        return {'series': series}


class SeasonView(TemplateView):
    template_name = 'archive/season_detail.html'

    def get_context_data(self, **kwargs):
        season_series = get_object_or_404(Series, slug = kwargs['series_slug'])
        season = get_object_or_404(Season, series = season_series, number = kwargs['season_num'])
        return {'season': season}


class EpisodeView(TemplateView):
    template_name = 'archive/episode_detail.html'

    def get_context_data(self, **kwargs):
        episode_series = get_object_or_404(Series, slug = kwargs['series_slug'])
        episode = get_object_or_404(Episode, series = episode_series, slug = kwargs['episode_slug'])
        return {'episode': episode}


class SeriesBrowseView(TemplateView):
    pass