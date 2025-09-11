from django.test import TestCase
from django.urls import reverse
from nexusapp_accounts.models import Account

class AccountModelTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(name="Test User", email="test@example.com")

    def test_account_creation(self):
        self.assertEqual(self.account.name, "Test User")
        self.assertEqual(self.account.email, "test@example.com")

class AccountViewsTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(name="View User", email="view@example.com")

    def test_account_list_view(self):
        response = self.client.get(reverse('account_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View User")

    def test_account_detail_view(self):
        response = self.client.get(reverse('account_detail', args=[self.account.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "view@example.com")
