from archive.models import Series
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class SeriesView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        series = get_object_or_404(Series, slug=kwargs['series_slug'])
        return {'series': series}
