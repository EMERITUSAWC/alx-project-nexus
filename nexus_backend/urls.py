from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Products app routes
    path('products/', include('nexusapp_products.urls')),
]
