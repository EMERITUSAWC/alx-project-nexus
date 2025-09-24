# nexusapp_accounts/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def accounts_list(request):
    # Replace this with actual account data when ready
    accounts = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Smith"},
    ]
    return render(request, 'accounts_list.html', {"accounts": accounts})

