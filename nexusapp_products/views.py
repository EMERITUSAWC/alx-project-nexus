from django.shortcuts import render
from .models import Product

def products_list(request):
    """Displays a list of all products."""
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})
