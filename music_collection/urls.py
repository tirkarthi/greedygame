from django.conf.urls import include, url
from rest_framework import routers

from .views import *


urlpatterns = [
    url(r'api/tracks/$', TrackViewSet.as_view()),
    url(r'api/genres/$', GenreViewSet.as_view()),
    url(r'api/tracks/(?P<pk>[0-9]+)$', TrackViewSetDetail.as_view()),
    url(r'api/genres/(?P<pk>[0-9]+)$', GenreViewSetDetail.as_view()),
    url(r'^tracks/$', TracksView.as_view(), name="track-list"),
    url(r'^tracks/(?P<pk>[0-9]+)$', TrackDetailView.as_view(), name="track-detail"),
    url(r'^genres/$', GenresView.as_view(), name="genre-list"),
    url(r'^genres/(?P<pk>[0-9]+)$', GenreDetailView.as_view(), name="genre-detail"),
]
