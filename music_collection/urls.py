from django.conf.urls import include, url
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
# router.register(r'tracks_api', TrackViewSet.as_view(), 'Track')
# router.register(r'genres_api', GenreViewSet.as_view(), 'Genre')

urlpatterns = [
    url(r'api/tracks', TrackViewSet.as_view()),
    url(r'api/genres', GenreViewSet.as_view()),
    url(r'^tracks', TracksView.as_view(), name="track-list"),
    url(r'^genres', GenresView.as_view(), name="genre-list"),
]
