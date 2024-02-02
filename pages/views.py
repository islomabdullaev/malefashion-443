from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# models
from pages.models import BannerModel
from products.models import ProductModel

# Create your views here
# FBV - Function Based View
# CBV - Class Based Views
class HomePageView(ListView):
    template_name = "home.html"
    model = BannerModel

    def get_queryset(self):
        return BannerModel.objects.filter(is_active=True)


class ShopPageView(ListView):
    template_name = "shop.html"
    model = ProductModel
    context_object_name = "products"


class AboutPageView(TemplateView):
    template_name = "about.html"


class BlogPageView(TemplateView):
    template_name = "blog.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"