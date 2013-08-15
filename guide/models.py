from django.db import models
from django.utils.text import slugify

class Place(models.Model):
    name = models.CharField(max_length=40)
    overview = models.TextField(blank=True, null=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Place, self).save(*args, **kwargs)

class Photo(models.Model):
    place = models.ForeignKey(Place)

    def __unicode__(self):
        return u'Photo %d at %s' % (self.id, self.place)

class Program(models.Model):
    place = models.ForeignKey(Place)
    location = models.CharField(max_length=40)
    for_credit = models.BooleanField()

    def __unicode__(self):
        return u'Program: %s at %s' % (self.location, self.place)

class Tip(models.Model):
    text = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=40, blank=True, null=True)
    place = models.ForeignKey(Place, null=True)
    program = models.ForeignKey(Program, null=True)

    def __unicode__(self):
        if self.place:
            location = self.place.__unicode__()
        elif self.program:
            location = self.program.__unicode__()
        else:
            location = ''
        return u'Tip: "%s" for %s' % (self.text, location)
