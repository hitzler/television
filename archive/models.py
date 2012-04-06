from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=255)