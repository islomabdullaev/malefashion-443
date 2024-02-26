from django.urls import path
from products.views import WishlistPageView, ShopDetailView, add_to_wishlist

app_name = "products"

urlpatterns = [
    path('<int:pk>/details/', ShopDetailView.as_view(), name="details"),
    path('wishlist/', WishlistPageView.as_view(), name="wishlist"),
    path('<int:product_pk>/add_to_wishlist/', add_to_wishlist, name="add_to_wishlist")
]