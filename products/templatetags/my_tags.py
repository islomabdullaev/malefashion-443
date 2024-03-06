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
def get_cart_info(request):
    cart = request.session.get("cart", [])
    if not cart:
        return 0, 0.0
    quantity, total_price = len(cart), ProductModel.get_from_cart(cart).aggregate(Sum("real_price"))['total_price']
    
    return quantity, round(total_price) if quantity and total_price else 0,0