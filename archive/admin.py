from archive.models import *
from django.contrib import admin
from slugify import slugify

class SeriesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'slug', 'network', 'language', 'country', 'description', 'imdb_id', 'genres')
        }),
        ('Airing Information', {
            'fields': ('premier', ('air_day', 'air_time'), 'runtime')
        }),
        ('Lock Options', {
            'classes': ('collapse',),
            'fields':  (('locked', 'locker'),)
        }),
    )
    list_display  = ['title', 'network']
    search_fields = ['title']
    prepopulated_fields =  {'slug': ['title']}

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)
        obj.save()


class EpisodeAdmin(admin.ModelAdmin):
    list_display  = ['title', 'series']
    search_fields = ['title', 'series']
    prepopulated_fields = {'slug': ['title']}

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)
        obj.save()


class NetworkAdmin(admin.ModelAdmin):
    list_display  = ['title', 'country']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}


class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields =  {'slug': ['title']}


admin.site.register(Series, SeriesAdmin)
admin.site.register(Season)
admin.site.register(Image)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Genre, GenreAdmin)