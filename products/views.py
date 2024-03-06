from typing import Any
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView

from products.models import ProductModel, WishlistModel

# Create your views here.

class WishlistPageView(ListView):
    template_name = 'wishlist.html'
    model = WishlistModel
    context_object_name = "wishlists"

    def get_queryset(self):
        return WishlistModel.objects.filter(user=self.request.user)


@login_required
def add_to_wishlist(request, product_pk):
    product = ProductModel.objects.get(pk=product_pk)
    current_url_path = request.META['HTTP_REFERER']
    try:
        WishlistModel.objects.create(user=request.user, product=product)
    except IntegrityError:
        WishlistModel.objects.get(user=request.user, product=product).delete()
    
    return redirect(current_url_path)

@login_required
def add_to_cart(request, pk):
    current_url_path = request.META['HTTP_REFERER']
    cart = request.session.get("cart", [])
    if pk in cart:
       cart.remove(pk) 
    else:
        cart.append(pk)
    request.session["cart"] = cart
    
    return redirect(current_url_path)


class ShopDetailView(DetailView):
    template_name = "shop-details.html"
    model = ProductModel
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_products"] = ProductModel.objects.filter(
            category__title=self.object.category.title).exclude(pk=self.object.pk)[:4]
        return context