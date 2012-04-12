from archive.models import Series
from django.shortcuts import get_object_or_404, render_to_response

def series_detail(request, series_slug):
    series = get_object_or_404(Series, slug=series_slug)
    return render_to_response('index.html',{'series': series})