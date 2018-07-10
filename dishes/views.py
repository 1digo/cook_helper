from django.shortcuts import render
from rest_framework import generics
from .serializers import DishSerializer
from .models import Dish


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new dish."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
