from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# models
from pages.models import BannerModel
from products.models import BrandModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel
from blogs.models import PostModel

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = ProductModel.objects.all()
        context["categories"] = CategoryModel.objects.all()
        context["brands"] = BrandModel.objects.all()
        context["sizes"] = SizeModel.objects.all()
        context["colors"] = ColorModel.objects.all()
        context["tags"] = TagModel.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"


class BlogPageView(ListView):
    template_name = "blog.html"
    model = PostModel
    context_object_name = "posts"

    def get_queryset(self):
        posts = PostModel.objects.all()
        tag = self.request.GET.get("tag")
        if tag:
            posts = PostModel.objects.filter(tags__title=tag)
        return posts


class ContactPageView(TemplateView):
    template_name = "contact.html"