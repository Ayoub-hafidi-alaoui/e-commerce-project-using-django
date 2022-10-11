from django.shortcuts import render
from products.models import Product
from .models import Cart, CartDetail

# Create your views here.


def add_to_cart(request):
    if request.method == 'post':
        product_id = request.POST["product_id"]
        quantity = request.POST["quantity"]
        product = Product.get(id=product_id)
        cart = Cart.objects.get(user=request.user, status='in progress')
        cart_detail, created = CartDetail.get_or_create(
            cart = cart,
            product= product
        )
        cart_detail.quantity = quantity
        cart_detail.price = product.price
        cart_detail.total = int(quantity) * product.price
        cart_detail.save()

