# urls.py at project root
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Simple view for root URL
def home(request):
    return render(request, "home.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('nexusapp_accounts.urls')),
    path('orders/', include('nexusapp_orders.urls')),
    path('products/', include('nexusapp_products.urls')),
    path('', home),  # <-- This serves the root URL
]
