from django.urls import path
from blogs.views import BlogDetailView, create_comment
app_name = "blogs"

urlpatterns = [
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('posts/<int:pk>/comment', create_comment, name='comment')
]