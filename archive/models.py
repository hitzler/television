from django.db import models

class Series(models.Model):
    title  = models.CharField(max_length=255)
    slug   = models.SlugField(max_length=255)
    # Aliases
    genres = models.ManyToManyField('Genre')

    # Start Date
    # Series Status
    # Series Air Day
    # Series Air Time
    # Series Country
    # Series Season Count
    network = models.ForeignKey('Network')
    locked  = models.BooleanField(default=False)
    locker  = models.ForeignKey('User')

class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)

class Network(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)
    # Country