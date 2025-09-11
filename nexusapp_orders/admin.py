from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'product', 'quantity', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('account__username', 'product__name')
    ordering = ('-created_at',)
