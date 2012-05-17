import os
import shutil

from television.settings import MEDIA_ROOT
from django.db import models
from django_countries import CountryField
from django.conf.global_settings import LANGUAGES
from django.contrib.auth.admin import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

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
SERIES_CHOICES = ((u'RUN', u'Running'), (u'END', u'Ended'))
GENDER_CHOICES = ((u'M', u'Male'), (u'F', u'Female'))
IMAGE_CHOICES  = ((0, 'poster'), (1, 'fanart'), (2, 'photo'))


class Series(models.Model):
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255)
    genres      = models.ManyToManyField('Genre')
    premier     = models.DateField(verbose_name='Date Premiered')
    air_day     = models.CharField(max_length=3, choices=DAY_CHOICES, verbose_name='Day Aired')
    air_time    = models.TimeField(verbose_name='Time Aired')
    network     = models.ForeignKey('Network')
    country     = CountryField()
    language    = models.CharField(max_length=7, choices=LANGUAGES)
    status      = models.CharField(max_length=3, choices=SERIES_CHOICES)
    description = models.TextField(blank=True, null=True)
    runtime     = models.IntegerField(default=0)
    imdb_id     = models.IntegerField(blank=True, max_length=7, default=0000000)
    locked      = models.BooleanField(default=False)
    locker      = models.ForeignKey(User, blank=True, null=True, verbose_name='Locked By')
    lock_msg    = models.TextField(blank=True, null=True)
    image       = generic.GenericRelation('Image')

    class Meta:
        verbose_name_plural = 'Series'

    def __unicode__(self):
        return u'%s' % self.title


class Season(models.Model):
    series   = models.ForeignKey('Series')
    number   = models.IntegerField(default=1)
    slug     = models.SlugField(blank=True, null=True, max_length=255)
    locked   = models.BooleanField(default=False)
    locker   = models.ForeignKey(User, blank=True, null=True, verbose_name='Locked By')
    lock_msg = models.TextField(blank=True, null=True)
    image    = generic.GenericRelation('Image')

    def __unicode__(self):
        return u'%s - Season %02d' % (self.series, self.number)

    def save(self, *args, **kwargs):
        self.slug = '%s-season-%02d' % (self.series.slug, self.number)
        super(Season, self).save(*args, **kwargs)


class Episode(models.Model):
    series      = models.ForeignKey('Series')
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255)
    season      = models.ForeignKey('Season')
    episode     = models.IntegerField(default=0)
    air_date    = models.DateField()
    description = models.TextField(blank=True, null=True)
    locked      = models.BooleanField(default=False)
    locker      = models.ForeignKey(User, blank=True, null=True, verbose_name='Locked By')
    lock_msg    = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('series', 'air_date', 'title')

    def __unicode__(self):
        return u'%s S%02dE%02d - %s' % (self.series, self.season.number, self.episode, self.title)


class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug  = models.CharField(max_length=70)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return u'%s' % self.title


class Network(models.Model):
    title   = models.CharField(max_length=70)
    slug    = models.CharField(max_length=70)
    country = CountryField()

    def __unicode__(self):
        return u'%s' % self.title


class Person(models.Model):
    name   = models.CharField(max_length=128)
    slug   = models.SlugField(max_length=128)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth  = models.DateField()
    death  = models.DateField(blank=True, null=True)
    image  = generic.GenericRelation('Image')

# Add roles to episodes.....
# Get rid of start end fields and get years from the first ep and last ep they are attached to
class Role(models.Model):
    name   = models.CharField(max_length=128)
    slug   = models.SlugField(max_length=128)
    actor  = models.ForeignKey('Person')
    series = models.ForeignKey('Series')
    start  = models.DateField(verbose_name='First Appearance')
    end    = models.DateField(verbose_name='Last Appearance')
    image  = generic.GenericRelation('Image')


class Image(models.Model):
    image          = models.ImageField(upload_to='tmp',)
    image_type     = models.IntegerField(max_length=1, choices=IMAGE_CHOICES)
    uploader       = models.ForeignKey(User, verbose_name='Uploaded By')
    content_type   = models.ForeignKey(ContentType)
    object_id      = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return u'%s - %s' % (self.content_object, self.image.name)

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)

        old_path   = os.path.join(MEDIA_ROOT, 'tmp', os.path.split(self.image.name)[1])
        self.image = new_path = self.create_path()
        shutil.move(old_path, os.path.join(MEDIA_ROOT, new_path))

        super(Image, self).save(*args, **kwargs)

    def create_path(self):
        categories = {8:'series', 9:'series', 13:'person', 14:'person'}
        # Pick category of image
        if self.content_type.name == 'series' or 'season':
            if self.content_type.name == 'series':
                parent = self.content_object.slug
            else:
                parent = self.content_object.series.slug
        elif self.content_type.name == 'person' or 'role':
            if self.content_type.name == 'person':
                parent = self.content_object.slug
            else:
                parent = self.content_object.person.slug

        # Create new path
        path = os.path.join('images', categories[self.content_type.id], parent[0], parent)
        if not os.path.exists(os.path.join(MEDIA_ROOT, path)):
            os.makedirs(os.path.join(MEDIA_ROOT, path))

        # Create new filename
        num  = 1
        file = '%s-%s-%02d%s' % (self.content_object.slug, IMAGE_CHOICES[self.image_type][1], num, os.path.splitext(self.image.name)[1])
        for files in os.listdir(os.path.join(MEDIA_ROOT, path)):
            if files.startswith(file):
                num += 1
                file = '%s-%s-%02d%s' % (self.content_object.slug, IMAGE_CHOICES[self.image_type][1], num, os.path.splitext(self.image.name)[1])
        return os.path.join(path, file)
