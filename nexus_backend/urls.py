from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from nexusapp_accounts import views as account_views

urlpatterns = [
    # Admin panel
    path("admin/", admin.site.urls),

    # Homepage
    path("", account_views.home, name="home"),

    # Accounts
    path("accounts/", account_views.account_list, name="account_list"),
    path("accounts/<int:pk>/", account_views.account_detail, name="account_detail"),
]

# Serve static files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
