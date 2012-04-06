from django.db import models

class Series(models.Model):
    title  = models.CharField(max_length=255)
    slug   = models.SlugField(max_length=255)
    #Aliases IDK M8
    genres = models.ManyToManyField('Genre')

class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)
