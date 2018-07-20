from django.db import models
from datetime import date


class Season(models.Model):
    name = models.CharField(max_length=6, blank=False, unique=True)
    # TODO Date diapason

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Dish(models.Model):
    """This class represents the dish model."""

    SOUP = 'SOUP'
    GARNISH = 'GARNISH'
    MEAT = 'MAIN'
    MAIN = 'MAIN'
    SALAD = 'SALAD'
    DISH_TYPE_CHOICES = (
        (SOUP, 'Soup'),
        (GARNISH, 'Garnish'),
        (MEAT, 'Meat'),
        (MAIN, 'Main'),
        (SALAD, 'Salad'),
    )

    LOW_DIFFICULTY = 1
    MEDIUM_DIFFICULTY = 2
    HIGH_DIFFICULTY = 3
    DIFFICULTY_CHOICES = (
        (LOW_DIFFICULTY, 'Low'),
        (MEDIUM_DIFFICULTY, 'Medium'),
        (HIGH_DIFFICULTY, 'High'),
    )

    name = models.CharField(max_length=255, blank=False, unique=True)
    dish_type = models.CharField(max_length=7, blank=False, choices=DISH_TYPE_CHOICES)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=MEDIUM_DIFFICULTY)
    season = models.ManyToManyField(Season, blank=False)
    priority = models.IntegerField(default=100)
    last_used_date = models.DateField(blank=True, null=True)

    # TODO ingredients = {'name': 'quantity'} ???
    # TODO description = textfield ???

    def add_date_of_today(self):
        self.last_used_date = date.today()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
