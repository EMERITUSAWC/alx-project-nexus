from django.shortcuts import render, get_object_or_404
from .models import Account

# Homepage view
def home(request):
    return render(request, 'index.html')

# List all accounts
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})

# Show details of a single account
def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'accounts/account_detail.html', {'account': account})
