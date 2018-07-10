from rest_framework import serializers
from .models import Dish


class DishSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dish
        fields = ('id', 'name', 'dish_type', 'season', 'difficulty')
        #read_only_fields = ('date_created', 'date_modified')
