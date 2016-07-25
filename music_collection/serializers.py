
from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('title', 'id', 'modified')


class TrackListingField(serializers.RelatedField):

    def to_representation(self, value):
        return '%s' % (value.title)


class TrackSerializer(serializers.ModelSerializer):
    genre = TrackListingField(many=True, read_only=True)

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        track = Track.objects.create(**validated_data)
        for genre in genres:
            try:
                genre_obj = Genre.objects.get(title=genre)
                genre_obj.track_set.add(track)
            except Genre.DoesNotExist:
                pass
        return track

    def update(self, instance, validated_data):
        genres = validated_data.pop('genre')
        instance.genre.clear()
        instance.title = validated_data.get('title', instance.title)
        instance.rating = validated_data.get('rating', instance.rating)
        for genre in genres:
            try:
                genre_obj = Genre.objects.get(title=genre)
                genre_obj.track_set.add(instance)
            except Genre.DoesNotExist:
                pass
        instance.save()
        return instance

    class Meta:
        model = Track
        fields = ('title', 'genre', 'rating', 'id', 'modified')
