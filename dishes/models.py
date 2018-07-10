from django.db import models


class Dish(models.Model):
    """This class represents the dish model."""
    DISH_TYPE_CHOICES = (
        ("SOUP", 'Soup'),
        ("GAR", 'Garnish'),
        ("MEAT", 'Meat'),
        ("MAIN", 'Main'),
        ("SAL", 'Salad'),
    )

    LOW_DIFFICULTY = 1
    MEDIUM_DIFFICULTY = 2
    HIGH_DIFFICULTY = 3
    DIFFICULTY_CHOICES = (
        (LOW_DIFFICULTY, 'Low'),
        (MEDIUM_DIFFICULTY, 'Medium'),
        (HIGH_DIFFICULTY, 'High'),
    )

    ANY_SEASON = 0
    WINTER_SEASON = 1
    SPRING_SEASON = 2
    SUMMER_SEASON = 3
    AUTUMN_SEASON = 4
    SEASON_CHOICES = (
        (ANY_SEASON, 'Any'),
        (WINTER_SEASON, 'Winter'),
        (SPRING_SEASON, 'Spring'),
        (SUMMER_SEASON, 'Summer'),
        (AUTUMN_SEASON, 'Autumn'),
    )

    name = models.CharField(max_length=255, blank=False, unique=True)
    dish_type = models.CharField(max_length=4, blank=False, choices=DISH_TYPE_CHOICES)
    season = models.IntegerField(choices=SEASON_CHOICES, default=ANY_SEASON)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=MEDIUM_DIFFICULTY)

    #ingredients = {'name': 'quantity'} ???

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
