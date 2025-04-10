from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import menuSerializer  # Ensure this exists
import json

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(Title="Burger", Price=50, Inventory=20)
        self.item2 = Menu.objects.create(Title="Pizza", Price=150, Inventory=10)

    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        items = Menu.objects.all()
        serializer = menuSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)

# python manage.py test restaurant.tests.test_views