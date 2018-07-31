from django.utils import six
from rest_framework import serializers, fields
from .models import Dish
from .choices import SEASON_CHOICES


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


class DishSerializer(DefaultModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    seasons = fields.MultipleChoiceField(choices=SEASON_CHOICES)
    # dish_type = serializers.CharField(source='get_dish_type_display')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dish

        fields = ('id', 'name', 'dish_type', 'seasons', 'difficulty', 'priority', 'last_used_date')

