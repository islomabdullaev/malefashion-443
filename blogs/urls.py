from django.urls import path
from blogs.views import BlogDetailView
app_name = "blogs"

urlpatterns = [
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='detail')
]