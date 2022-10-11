from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from utils.generate_code import generate_code
from products.models import Product

# Create your models here.



CART_STATUS_CHOICES = (
    ("in progress", "in progress"),
    ("completed", "completed"),
)
class Cart(models.Model):
    code = models.CharField(max_length=8, default=generate_code)
    user = models.ForeignKey(User, related_name="user_cart", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=CART_STATUS_CHOICES, max_length=15)

    def __str__(self):
        return self.code


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_detail", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_cart", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.order)




STATUS_CHOICES = (
    ("received", "received"),
    ("processed", "processed"),
    ("delivered", "delivered"),
)


class Order(models.Model):
    code = models.CharField(max_length=8, default=generate_code)
    user = models.ForeignKey(User, related_name="user_order", on_delete=models.SET_NULL, null=True, blank=True)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=11)

    def __str__(self):
        return self.code


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name="order_detail", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_order", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.order)
