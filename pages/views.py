from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView

# models
from pages.models import BannerModel
from products.models import BrandModel, CategoryModel, ColorModel, CouponModel, ProductModel, SizeModel, TagModel
from blogs.models import PostModel
from django.db.models import Max, Min

from products.utils import get_price_range


# Create your views here
# FBV - Function Based View
# CBV - Class Based Views
class HomePageView(ListView):
    template_name = "home.html"
    model = BannerModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = ProductModel.objects.all()[:8]
        context["posts"] = PostModel.objects.all()

        return context

    def get_queryset(self):
        return BannerModel.objects.filter(is_active=True)


class ShopPageView(ListView):
    template_name = "shop.html"
    model = ProductModel
    context_object_name = "products"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["brands"] = BrandModel.objects.all()
        context["sizes"] = SizeModel.objects.all()
        context["colors"] = ColorModel.objects.all()
        context["tags"] = TagModel.objects.all()
        context["min_price"] = ProductModel.objects.aggregate(min_price=Min('price'))['min_price']
        context["max_price"] = ProductModel.objects.aggregate(min_price=Max('price'))['min_price']
        my_range = self.request.GET.get("my_range")
        price_range = get_price_range(price_range=my_range)
        if price_range:
            from_price, to_price = price_range[0], price_range[1]
            context['from_price'], context['to_price'] = from_price, to_price
        return context
    
    def get_queryset(self):
        products = ProductModel.objects.all().order_by('price')
        q = self.request.GET.get("q")
        tag = self.request.GET.get("tag")
        sort = self.request.GET.get("sort")
        category = self.request.GET.get("category")
        brand = self.request.GET.get("brand")
        color = self.request.GET.get("color")
        size = self.request.GET.get("size")
        min_price = ProductModel.objects.aggregate(min_price=Min('price'))['min_price']
        max_price = ProductModel.objects.aggregate(min_price=Max('price'))['min_price']
        from_price, to_price = min_price, max_price
        my_range = self.request.GET.get("my_range")
        price_range = get_price_range(price_range=my_range)
        if price_range:
            self.paginate_by = products.all().count()
            from_price, to_price = price_range[0], price_range[1]

        if q:
            products = products.filter(name__icontains=q)
        elif tag:
            products = products.filter(tags__title=tag)
        elif category:
            products = products.filter(category__title=category)
        elif brand:
            products = products.filter(brand__title=brand)
        elif size:
            products = products.filter(size__title=size)
        elif color:
            products = products.filter(colors__name=color)
        elif sort:
            products = products.order_by(sort)
        elif my_range:
            products = products.filter(price__range=[from_price, to_price])
        return products


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


class CartListView(ListView):
    template_name = 'shopping-cart.html'
    model = ProductModel
    context_object_name = "products"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        code = self.request.GET.get("coupon")
        try:
            coupon = CouponModel.objects.get(code=code)
            context['coupon'] = coupon
        except CouponModel.DoesNotExist:
            context['coupon'] = None
        
        return context

    def get_queryset(self):
        cart = self.request.session.get("cart", [])
        products = ProductModel.objects.filter(pk__in=cart)
        
        return products