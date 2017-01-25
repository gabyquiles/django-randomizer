from django.test import TestCase
from .models import Restaurant

# Create your tests here.
class TestRandomizer(TestCase):

    def test_homepage(self):
        r1 = Restaurant.objects.create(name="Bob's Diner")
        r2 = Restaurant.objects.create(name="Jill's Diner")
        restaurants = Restaurant.objects.all()
        response = self.client.get('/')
        # self.assertEquals(response.context['restaurant'], [])
        self.assertIn(response.context['restaurant'], restaurants)