from django.db import models
from nexusapp_accounts.models import Account
from nexusapp_products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # ✅ Added
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Added for admin ordering

    def __str__(self):
        return f"Order #{self.id} - {self.account.username} - {self.product.name}"
