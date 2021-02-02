from django.http import request
from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):

        product_id = request.session.get('cart').keys()
        data = {}
        data['products'] = Product.get_product_by_ids_list(product_id)
        return render(request, 'store/cart.html', data)
