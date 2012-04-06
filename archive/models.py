from django.db import models

class Series(models.Model):
    title  = models.CharField(max_length=255)
    slug   = models.SlugField(max_length=255)
    # Aliases
    genres = models.ManyToManyField('Genre')
    # Start Date
    # Series Status
    # Series Original Network
    # Series Air Day
    # Series Air Time
    # Series Country
    # Series Season Count
    # Series Locked (Y/N)

class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)
