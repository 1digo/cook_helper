from django.db import models
from datetime import date
from .choices import *
from multiselectfield import MultiSelectField


class Dish(models.Model):
    """This class represents the dish model."""

    name = models.CharField(max_length=255, blank=False, unique=True)
    dish_type = models.CharField(max_length=7, blank=False, choices=DISH_TYPE_CHOICES)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=MEDIUM_DIFFICULTY)
    seasons = MultiSelectField(choices=SEASON_CHOICES)
    priority = models.IntegerField(default=100)
    raw = models.CharField(max_length=30, null=True)
    is_post = models.BooleanField(default=False)
    is_diet = models.BooleanField(default=False)
    last_used_date = models.DateField('last use date', null=True)

    def __unicode__(self):
        return self.name

    # TODO ingredients = [{'name': 'quantity'},...]

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
