from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# import all the models
# importing JsonResponse so that we can return a message
# Create your views here.


def store(request):
    products = Product.objects.all()
    # we will use products using the context dictionary
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    # user logged in -> authenticated
    if request.user.is_authenticated:
        customer = request.user.customer

        # first query with a value, if it exists, then get it; otherwise create it
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        # it will get all the items that have the 'order' as the parent
        items = order.orderitem_set.all()
    else:
        # user not logged in -> unauthenticated
        # return an empty value
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:

        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    return JsonResponse("Item was added", safe=False)
