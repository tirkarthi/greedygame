from django.db import models

# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=200)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)


class Track(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(default=4)
    genre = models.ManyToManyField(Genre)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
