from django.shortcuts import redirect, render
from django.views import View
from store.models.oder import Oder


class Oders(View):
    def get(self, request):
        customer_id = request.session.get('customer_id')
        oders = Oder.get_products_by_customer_id(customer_id)
        return render(request, 'store/oders.html', {'oders': oders})
