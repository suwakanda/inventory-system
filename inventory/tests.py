from django.test import TestCase
from django.urls import reverse
from .models import Inventory, Supplier

class InventoryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        supplier = Supplier.objects.create(name="Test Supplier")
        Inventory.objects.create(
            name="Test Item",
            description="Test Description",
            note="Test Note",
            stock=10,
            availability=True,
            supplier=supplier
        )

    def test_list_view_status(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)

    def test_api_status(self):
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_status(self):
        item = Inventory.objects.first()
        response = self.client.get(f'/inventory/{item.id}/')
        self.assertEqual(response.status_code, 200)