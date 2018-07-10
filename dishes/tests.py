from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Dish


class ModelTestCase(TestCase):
    """This class defines the test suite for the dish model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.dish_name = "Tuna"
        self.dish = Dish(name=self.dish_name)

    def test_model_can_create_a_dish(self):
        """Test the dish model can create a dish."""
        old_count = Dish.objects.count()
        self.dish.save()
        new_count = Dish.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.dish_data = {'name': 'Tuna', 'dish_type': 'MEAT'}
        self.response = self.client.post(
            reverse('create'),
            self.dish_data,
            format="json")

    def test_api_can_create_a_dish(self):
        """Test the api has dish creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_dish(self):
        """Test the api can get a given dish."""
        dish = Dish.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': dish.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, dish)

    def test_api_can_update_dish(self):
        """Test the api can update a given dish."""
        dish = Dish.objects.get()
        change_dish = {'name': 'Something new',
                       'dish_type': 'SOUP',
                       'season': Dish.SUMMER_SEASON,
                       'difficulty': Dish.LOW_DIFFICULTY}
        res = self.client.put(
            reverse('details', kwargs={'pk': dish.id}),
            change_dish, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_dish(self):
        """Test the api can delete a dish."""
        dish = Dish.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': dish.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
