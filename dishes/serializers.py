from django.utils import six
from rest_framework import serializers, fields
from .models import Dish, Season


class ChoiceDisplayField(fields.ChoiceField):
    def __init__(self, *args, **kwargs):
        super(ChoiceDisplayField, self).__init__(*args, **kwargs)
        self.choice_strings_to_display = {
            six.text_type(key): value for key, value in self.choices.items()
        }

    def to_representation(self, value):
        if value is None:
            return value
        return {
            'value': self.choice_strings_to_values.get(six.text_type(value), value),
            'display': self.choice_strings_to_display.get(six.text_type(value), value),
        }


class DefaultModelSerializer(serializers.ModelSerializer):
    serializer_choice_field = ChoiceDisplayField


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('id', 'name',)


class DishSerializer(DefaultModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    season = SeasonSerializer(many=True)
    # dish_type = serializers.CharField(source='get_dish_type_display')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dish

        fields = ('id', 'name', 'dish_type', 'season', 'difficulty', 'priority', 'last_used_date')
