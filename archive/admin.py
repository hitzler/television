from archive.models import *
from django.contrib import admin

class SeriesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'slug', 'network', 'country', 'language', 'genres')
        }),
        ('Airing Information', {
            'fields': ('premier', ('airDay', 'airTime'))
        }),
        ('Lock Options', {
            'classes': ('collapse',),
            'fields':  (('locked', 'locker'),)
        }),
    )
    list_display  = ['title', 'network']
    search_fields = ['title']
    prepopulated_fields =  {'slug': ['title']}

class EpisodeAdmin(admin.ModelAdmin):
    list_display  = ['title', 'series']
    search_fields = ['title', 'series']
    prepopulated_fields = {'slug': ['title']}

class NetworkAdmin(admin.ModelAdmin):
    list_display  = ['title', 'country']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}

class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields =  {'slug': ['title']}

#
admin.site.register(Series, SeriesAdmin)
admin.site.register(Season)
admin.site.register(Image)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Genre, GenreAdmin)