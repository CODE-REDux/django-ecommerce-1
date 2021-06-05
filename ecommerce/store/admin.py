from django.contrib import admin
from .models import *
# import all the models that we have defined: Customer, Product, Order, OrderItem, ShippingAddress
# Register your models here.


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
