from django.db import models
from django.contrib.auth.admin import User
DAY_CHOICES = (
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
    ('WEK', 'Weekdays'),
    ('DAL', 'Daily')
)

class Series(models.Model):
    title   = models.CharField(max_length=255)
    slug    = models.SlugField(max_length=255)
    genres  = models.ManyToManyField('Genre')
    premier = models.DateField(verbose_name='Date Premiered')
    airDay  = models.CharField(max_length=3, choices=DAY_CHOICES, verbose_name='Day Aired')
    airTime = models.TimeField(verbose_name='Time Aired')
    seasons = models.IntegerField()
    network = models.ForeignKey('Network')
    locked  = models.BooleanField(default=False)
    locker  = models.ForeignKey(User, verbose_name='Locked By')
    # Series Status
    # Series Country
    class Meta:
        verbose_name_plural = 'Series'

class Episode(models.Model):
    series  = models.ForeignKey('Series')
    title   = models.CharField(max_length=255)
    slug    = models.SlugField(max_length=255)
    season  = models.IntegerField(default=0)
    episode = models.IntegerField(default=0)
    airDate = models.DateField()

    class Meta:
        unique_together = ('series', 'airDate', 'title')
    def __unicode__(self):
        return u'%s S%02dE%02d - %s' % (self.series, self.season, self.episode, self.title)

class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)

class Network(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)
    # Country
















