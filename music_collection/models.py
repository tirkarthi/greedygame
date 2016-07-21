from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=200)


class Track(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(default=4)
    genre = models.ManyToManyField(Genre)
