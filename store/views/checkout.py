from store.models.customer import Customer
from store.models.oder import Oder
from django.shortcuts import redirect
from django.views import View
from store.models.product import Product


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_product_by_ids_list(cart.keys())
        for product in products:
            oder = Oder(
                product=product,
                customer=Customer(id=customer),
                quantity=cart.get(str(product.id)),
                price=product.price,
                address=address,
                phone_number=phone,
            )
            Oder.placeOder(oder)
        request.session['cart'] = {}
        return redirect('cart')
