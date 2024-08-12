from django.shortcuts import render
from products.models import Product


def products_display(request):
    products = Product.objects.all()
    data = {'products': products}
    return render(request, 'products_display.html', context=data)
