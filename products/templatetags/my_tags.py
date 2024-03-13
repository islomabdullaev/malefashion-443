from django import template

from products.models import ProductModel, WishlistModel
from django.db.models import Sum

register = template.Library()

# @register.simple_tag(name="get_rating_range")
# def get_rating_range(value):
#     rating_len = []
#     for i in range(value):
#         rating_len.append(i)

#     return rating_len


# @register.simple_tag(name="python")
# def python(value):
#     return "python lang"

@register.filter(name="in_wishlist")
def in_wishlist(user, product):
    return WishlistModel.objects.filter(user=user, product=product).exists()


@register.simple_tag
def get_cart_info(request, coupon=None):
    cart = request.session.get("cart", [])
    if not cart:
        return 0, 0.0
    products = ProductModel.get_from_cart(cart)
    total_price = 0
    quantity = len(cart)
    for product in products:
        total_price += float(product.get_real_price())
    if coupon:
        total_price = total_price - ((total_price / 100) * float(coupon.discount))
    return quantity, "{:.2f}".format(total_price)