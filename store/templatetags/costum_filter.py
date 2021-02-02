from store.models.customer import Customer
from django import template

register = template.Library()


@register.filter(name='rupee')
def rupee(number):
    return '₹ '+str(number)


@register.filter(name='get_customer_by_id')
def get_customer_by_id(id):
    return Customer.get_customer_by_id(id)


@register.filter(name='multiply')
def multiply(a, b):
    return a * b


# @register.filter(name='total_item_in_cart')
# def total_item_in_cart(cart):
#     cart = cart.values()
#     print(cart)
#     sum = 0
#     for i in cart:
#         sum += 1
#     return sum
