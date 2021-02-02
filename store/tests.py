from django.test import TestCase

# Create your tests here.
from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.
product_id = request.POST.get('product_id')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1