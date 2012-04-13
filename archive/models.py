from django.db import models
from django_countries import CountryField
from django.conf.global_settings import LANGUAGES
from django.contrib.auth.admin import User

DAY_CHOICES = (
    (u'MON', u'Monday'),
    (u'TUE', u'Tuesday'),
    (u'WED', u'Wednesday'),
    (u'THU', u'Thursday'),
    (u'FRI', u'Friday'),
    (u'SAT', u'Saturday'),
    (u'SUN', u'Sunday'),
    (u'WEK', u'Weekdays'),
    (u'DAL', u'Daily')
)
SERIES_CHOICES = ((u'RUN', u'Running'),(u'END', u'Ended'),)

class Series(models.Model):
    title    = models.CharField(max_length=255)
    slug     = models.SlugField(max_length=255)
    genres   = models.ManyToManyField('Genre')
    premier  = models.DateField(verbose_name='Date Premiered')
    airDay   = models.CharField(max_length=3, choices=DAY_CHOICES, verbose_name='Day Aired')
    airTime  = models.TimeField(verbose_name='Time Aired')
    network  = models.ForeignKey('Network')
    country  = CountryField()
    language = models.CharField(max_length=7, choices=LANGUAGES)
    status   = models.CharField(max_length=3, choices=SERIES_CHOICES)
    locked   = models.BooleanField(default=False)
    locker   = models.ForeignKey(User, blank=True, null=True, verbose_name='Locked By')

    class Meta:
        verbose_name_plural = 'Series'
    def __unicode__(self):
        return u'%s' % self.title

class Season(models.Model):
    series = models.ForeignKey('Series')
    season = models.IntegerField()
    locked = models.BooleanField(default=False)
    locker = models.ForeignKey(User, blank=True, null=True, verbose_name='Locked By')

    def __unicode__(self):
        return u'%s - Season %02d' % (self.series, self.season)

class Episode(models.Model):
    series  = models.ForeignKey('Series')
    title   = models.CharField(max_length=255)
    slug    = models.SlugField(max_length=255)
    season  = models.ForeignKey('Season', limit_choices_to={'series': '1'})
#    season  = models.IntegerField(default=0)
    episode = models.IntegerField(default=0)
    airDate = models.DateField()

    class Meta:
        unique_together = ('series', 'airDate', 'title')
    def __unicode__(self):
        return u'%s S%02dE%02d - %s' % (self.series, self.season.season, self.episode, self.title)

class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)

    def __unicode__(self):
        return u'%s' % self.title

class Network(models.Model):
    title   = models.CharField(max_length=70)
    slug    = models.CharField(max_length=70)
    country = CountryField()

    def __unicode__(self):
        return u'%s' % self.title

class Person(models.Model):
    name  = models.CharField(max_length=128)
    slug  = models.SlugField(max_length=128)
    birth = models.DateField()
    death = models.DateField(blank=True, null=True)


class Role(models.Model):
    name   = models.CharField(max_length=128)
    slug   = models.SlugField(max_length=128)
    actor  = models.ForeignKey('Person')
    series = models.ForeignKey('Series')
    start  = models.DateField(verbose_name='First Appearance')
    end    = models.DateField(verbose_name='Last Appearance')



