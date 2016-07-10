from django.db import models

# Create your models here.

class Genre(models.Model):
    Title = models.CharField(max_length=200)


class Track(models.Model):
    Title = models.CharField(max_length=200)
    Rating = models.IntegerField(default=4)
    Genre = models.ManyToManyField(Genre)
