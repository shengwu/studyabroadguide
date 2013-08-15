from django.db import models
from django.utils.text import slugify

class Place(models.Model):
    name = models.CharField(max_length=40)
    overview = models.TextField(blank=True, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Place, self).save(*args, **kwargs)

class Photo(models.Model):
    place = models.ForeignKey(Place)

class Program(models.Model):
    place = models.ForeignKey(Place)
    location = models.CharField(max_length=40)
    for_credit = models.BooleanField()

class Tip(models.Model):
    text = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=40, blank=True, null=True)
    place = models.ForeignKey(Place, null=True)
    program = models.ForeignKey(Program, null=True)
