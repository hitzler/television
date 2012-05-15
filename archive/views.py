from archive.models import Series, Season
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class SeriesView(TemplateView):
    template_name = 'archive/series_detail.html'

    def get_context_data(self, **kwargs):
        series = get_object_or_404(Series, slug=kwargs['series_slug'])
        return {'series': series}


class SeasonView(TemplateView):
    template_name = 'archive/series_detail.html'

    def get_context_data(self, **kwargs):
        season_series = Series.objects.get(slug = kwargs['series_slug'])
        season = Season.objects.filter(series = season_series)


class EpisodeView(TemplateView):
    template_name = 'archive/series_detail.html'

    def get_context_data(self, **kwargs):
        pass