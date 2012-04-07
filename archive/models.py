from django.db import models
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
    airDay  = models.CharField(max_length=3, choices=DAY_CHOICES)
    seasons = models.IntegerField()
    network = models.ForeignKey('Network')
    locked  = models.BooleanField(default=False)

    #locker = models.ForeignKey('User')
    # Start Date
    # Series Status
    # Series Air Time
    # Series Country
    class Meta:
        verbose_name_plural = 'Series'

class Episode(models.Model):
    series  = models.ForeignKey('Series')
    title   = models.CharField(max_length=255)
    slug    = models.SlugField(max_length=255)
    season  = models.IntegerField(default=0)
    episode = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s S%02dE%02d - %s' % (self.series, self.season, self.episode, self.title)

class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)

class Network(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)
    # Country