from django.db import models
from django.contrib.auth.models import User

# validators
from products.validators import rating_value_validate

# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class BrandModel(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class SizeModel(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"


class ColorModel(models.Model):
    name = models.CharField(max_length=24)
    code = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.name}|{self.code}"
    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class TagModel(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class ProductModel(models.Model):
    name = models.CharField(max_length=36)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    rating = models.PositiveIntegerField(default=1, validators=[rating_value_validate])
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(SizeModel)
    colors = models.ManyToManyField(ColorModel)
    tags = models.ManyToManyField(TagModel)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class WishlistModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
        unique_together = ['user', 'product']

    def __str__(self) -> str:
        return f"{self.user.username} | {self.product.name}"
    
