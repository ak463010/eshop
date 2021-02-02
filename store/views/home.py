from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):
    def post(self, request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')

        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = cart.get(product_id) - 1
                else:
                    cart[product_id] = cart.get(product_id) + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1

        request.session['cart'] = cart
        return redirect('store')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categoryies = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_all_products_by_category_id(category_id)
        else:
            products = Product.get_all_products()

        context = {}
        context['products'] = products
        context['categories'] = categoryies
        return render(request, 'store/index.html', context)
