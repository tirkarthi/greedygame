
from rest_framework import serializers
from .models import *


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('Title', 'Genre', 'Rating')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('Title', )
