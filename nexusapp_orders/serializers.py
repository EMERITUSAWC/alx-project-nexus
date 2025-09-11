from rest_framework import serializers
from .models import Order
from nexusapp_accounts.serializers import AccountSerializer
from nexusapp_products.serializers import ProductSerializer
from nexusapp_accounts.models import Account
from nexusapp_products.models import Product

class OrderSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    account_id = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), write_only=True, source='account'
    )
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, source='product'
    )

    class Meta:
        model = Order
        fields = ("id", "account", "account_id", "product", "product_id", "quantity", "status", "created_at")
        read_only_fields = ("id", "created_at", "status")
