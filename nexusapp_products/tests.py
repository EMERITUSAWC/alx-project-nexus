from django.test import TestCase
from django.urls import reverse
from nexusapp_products.models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Laptop", description="A test laptop", price=999.99)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, 999.99)

class ProductViewsTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Phone", description="Smartphone", price=599.99)

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Phone")

    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Smartphone")
