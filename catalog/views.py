from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Address


def home(request):
    products = Product.objects.all()[:5]
    return render(request, 'catalog/home.html', {'products': products})


def contacts(request):
    address = Address.objects.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html', {'address': address})
