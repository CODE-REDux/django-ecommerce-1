from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# customer model


class Customer(models.Model):
    # for one customer -> one user (vice-versa)
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# model for product


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    # if is digital, it can't be shipped
    digital = models.BooleanField(default=False, null=True, blank=True)
    # image

    def __str__(self):
        return self.name

# model for order


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True)
    transaction_id = models.CharField(max_length=100, null=True)

    # to return a string, we have used str() on self.id
    def __str__(self):
        return str(self.id)

# an item can be selected mor than once


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True, )
    date_added = models.DateTimeField(auto_now_add=True)


# shipping model : to get customer info, billing info etc
class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    # Issue : what about country ?
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
