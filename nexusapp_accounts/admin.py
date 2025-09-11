from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')  # ✅ use 'name' instead of 'username'

admin.site.register(Account, AccountAdmin)
