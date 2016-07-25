from rest_framework import generics, status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics
from django.views.generic import View, ListView, DetailView
from django.conf import settings


class TracksView(ListView):

    model = Track

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_size'] = settings.REST_FRAMEWORK['PAGE_SIZE']
        return context


class TrackDetailView(DetailView):

    model = Track

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GenresView(ListView):

    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_size'] = settings.REST_FRAMEWORK['PAGE_SIZE']
        return context


class GenreDetailView(DetailView):

    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrackViewSet(generics.ListCreateAPIView):
    serializer_class = TrackSerializer

    def post(self, request, format=None):
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(genre=request.data.get('genre', []))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Track.objects.all().order_by('-modified')
        title = self.request.query_params.get('title')
        rating = self.request.query_params.get('rating')
        genre = self.request.query_params.get('genre')
        if title:
            queryset = queryset.filter(title__contains=title)
        if rating:
            queryset = queryset.filter(rating__gte=rating)

        return queryset


class TrackViewSetDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrackSerializer

    def get_object(self, pk):
        try:
            return Track.objects.get(id=pk)
        except Track.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Track = self.get_object(pk)
        serializer = TrackSerializer(Track)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        track = self.get_object(pk)
        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save(genre=request.data.get('genre', []))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        track = self.get_object(pk)
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreViewSet(generics.ListCreateAPIView):
    serializer_class = GenreSerializer

    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Genre.objects.all().order_by('-modified')
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__contains=title)

        return queryset


class GenreViewSetDetail(generics.ListCreateAPIView):
    serializer_class = GenreSerializer

    def get_object(self, pk):
        try:
            return Genre.objects.get(id=pk)
        except Track.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Genre = self.get_object(pk)
        serializer = GenreSerializer(Genre)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        genre = Genre.objects.get(id=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
