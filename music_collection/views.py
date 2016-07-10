from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics
from django.views.generic import View, ListView

# Create your views here.

class TracksView(ListView):

    model = Track

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GenresView(ListView):

    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
class IndexView(View):

    def get(self, request):
        return HttpResponse("Hello home")


class TrackViewSet(generics.ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        queryset = Track.objects.all()
        title = self.request.query_params.get('title')
        rating = self.request.query_params.get('rating')
        genre = self.request.query_params.get('genre')
        if title:
            queryset = queryset.filter(Title__contains=title)
        if rating:
            queryset = queryset.filter(Rating__gte=rating)
        if genre:
            queryset = queryset.filter(Genre=Genre.objects.filter(Title=genre))

        return queryset


class GenreViewSet(generics.ListAPIView):
    serializer_class = GenreSerializer

    def get_queryset(self):
        queryset = Genre.objects.all()
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(Title__contains=title)

        return queryset
