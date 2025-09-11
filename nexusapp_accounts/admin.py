from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'created_at')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)
