from django.shortcuts import render
from rest_framework import generics
from .serializers import DishSerializer, SeasonSerializer
from .models import Dish, Season


class DishesCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new dish."""
        serializer.save()


class DishesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class SeasonsCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new season."""
        serializer.save()


class SeasonsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
