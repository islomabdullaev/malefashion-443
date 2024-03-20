from django.http import HttpResponse
from django.shortcuts import redirect, render

from orders.models import OrderItemModel, OrderModel
from products.models import CouponModel, ProductModel

# Create your views here.

def checkout(request):
    if request.method == "POST":
        cart = request.session.get("cart", [])
        total_price = float(request.GET.get("total_price"))
        code = request.GET.get("code")
        if code:
            try:
                coupon = CouponModel.objects.get(code=code)
                coupon.is_active = False
                coupon.save()
            except CouponModel.DoesNotExist:
                coupon = None
        if not cart:
            return HttpResponse("Cart is Empty !")
        products = ProductModel.get_from_cart(cart=cart)
            
        order = OrderModel.objects.create(user=request.user, total_price=total_price)
        for product in products:
            OrderItemModel.objects.create(product=product, quantity=1, order=order)

    return redirect('pages:cart')