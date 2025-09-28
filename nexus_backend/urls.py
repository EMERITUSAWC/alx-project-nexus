from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nexusapp_accounts.urls')),  # Root URL
    path('orders/', include('nexusapp_orders.urls')),
    path('products/', include('nexusapp_products.urls')),
]
