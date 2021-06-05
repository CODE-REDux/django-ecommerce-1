from django.shortcuts import render
from .models import *
# import all the models

# Create your views here.


def store(request):
    products = Product.objects.all()
    # we will use products using the context dictionary
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
