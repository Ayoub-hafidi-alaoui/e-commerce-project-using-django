from django.contrib import admin

# Register your models here.

from .models import Order, OrderDetails, Cart, CartDetail

admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Cart)
admin.site.register(CartDetail)
