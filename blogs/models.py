from django.db import models

from products.models import TagModel

# Create your models here.

class AuthorModel(models.Model):
    full_name = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to="authors/avatar")
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class PostModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    short_description = models.TextField(null=True)
    image = models.ImageField(upload_to="posts")
    tags = models.ManyToManyField(TagModel)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"