from typing import Any
from django.db import IntegrityError
from django.shortcuts import redirect, render

from django.views.generic import ListView

from products.models import ProductModel, WishlistModel

# Create your views here.

class WishlistPageView(ListView):
    template_name = 'wishlist.html'
    model = WishlistModel
    context_object_name = "wishlists"

    def get_queryset(self):
        return WishlistModel.objects.filter(user=self.request.user)


def add_to_wishlist(request, product_pk):
    product = ProductModel.objects.get(pk=product_pk)
    current_url_path = request.META['HTTP_REFERER']
    try:
        WishlistModel.objects.create(user=request.user, product=product)
    except IntegrityError:
        WishlistModel.objects.get(user=request.user, product=product).delete()
    
    return redirect(current_url_path)
