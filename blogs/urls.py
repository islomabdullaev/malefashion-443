from django.urls import path
from blogs.views import BlogDetailView, CommentCreateView
app_name = "blogs"

urlpatterns = [
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('posts/<int:pk>/comment', CommentCreateView.as_view(), name='comment')
]