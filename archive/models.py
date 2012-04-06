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
    airDay  = models.CharField(max_length=2, choices=DAY_CHOICES)
    seasons = models.IntegerField()
    network = models.ForeignKey('Network')
    locked  = models.BooleanField(default=False)

    #locker = models.ForeignKey('User')
    # Start Date
    # Series Status
    # Series Air Time
    # Series Country

class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)

class Network(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)
    # Country