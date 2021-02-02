from django import template
register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    for id in cart.keys():
        if int(id) == product.id:
            return True
    return False


# my created function
@register.filter(name='quantity')
def quantity(product, cart):
    product_id = product.id
    return cart.get(str(product_id))
# my createed functon


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    for id in cart.keys():
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='product_quantity_price')
def product_quantity_price(product, cart):
    total = quantity(product, cart)
    return total * product.price


@register.filter(name='total_price')
def total_price(products, cart):
    sum = 0
    for product in products:
        sum += product.price * quantity(product, cart)
    return sum
