from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Burger", price=10, inventory=50)
        self.menu2 = Menu.objects.create(title="Pizza", price=15, inventory=30)
        self.menu3 = Menu.objects.create(title="Pasta", price=12, inventory=40)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')  # Replace with your actual URL
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)