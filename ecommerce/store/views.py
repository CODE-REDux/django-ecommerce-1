from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
# import all the models
# importing JsonResponse so that we can return a message
# Create your views here.


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
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
        cartItems = order.get_cart_items

    else:
        # manually set all the values for the guest user
        # user not logged in -> unauthenticated
        # return an empty value
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        print("order.shipping:", order.shipping)
    else:

        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}

    return render(request, 'store/checkout.html', context)


def updateItem(request):
    #  parse the data, as we are sending it as a string
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("Action: ", action)
    print("productId: ", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    if action == 'add':
        return JsonResponse("Item was added", safe=False)
    elif action == 'remove':
        return JsonResponse("Item was removed", safe=False)
