from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('nexusapp_accounts.urls')),
    path('orders/', include('nexusapp_orders.urls')),
    path('products/', include('nexusapp_products.urls')),
]
