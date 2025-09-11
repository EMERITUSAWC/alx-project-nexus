from django.test import TestCase
from django.urls import reverse
from nexusapp_orders.models import Order
from nexusapp_accounts.models import Account
from nexusapp_products.models import Product

class OrderModelTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(name="Order User", email="order@example.com")
        self.product = Product.objects.create(name="Tablet", description="Test Tablet", price=299.99)
        self.order = Order.objects.create(account=self.account, product=self.product, quantity=2, status="Pending")

    def test_order_creation(self):
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.status, "Pending")

class OrderViewsTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(name="View Order", email="vieworder@example.com")
        self.product = Product.objects.create(name="Monitor", description="4K Monitor", price=399.99)
        self.order = Order.objects.create(account=self.account, product=self.product, quantity=1, status="Shipped")

    def test_order_list_view(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Monitor")

    def test_order_detail_view(self):
        response = self.client.get(reverse('order_detail', args=[self.order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shipped")
