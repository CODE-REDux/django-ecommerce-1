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


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    # if is digital, it can't be shipped and default is set to false
    digital = models.BooleanField(default=False, null=True, blank=True)
    # image
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    # when we don't have url for an image, it would send an empty url,
    # and prevent the whole page from crashing, when image url is absent.

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True)
    transaction_id = models.CharField(max_length=100, null=True)

    # to return a string, we have used str() on self.id
    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
                break
        return shipping

    # get_card_total is dependent on get_total -> so, we first wrote get_total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True, )
    date_added = models.DateTimeField(auto_now_add=True)

    # property decorator used
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
        # now, we can call this quantity in the template 'cart.html'


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
