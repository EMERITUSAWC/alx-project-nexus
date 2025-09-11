from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('nexusapp_accounts.urls')),
    path('products/', include('nexusapp_products.urls')),
    path('orders/', include('nexusapp_orders.urls')),
    path('', RedirectView.as_view(url='/accounts/', permanent=False)),  # Redirect root URL to /accounts/
]
