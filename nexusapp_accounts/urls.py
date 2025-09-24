# nexusapp_accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Accounts list view
    path('accounts/', views.accounts_list, name='accounts_list'),
]
