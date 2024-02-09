from django.shortcuts import render

from blogs.models import PostModel
from django.views.generic import DetailView

# Create your views here.
# Blog detail fbv
"""
def post_detail(request, pk):
    post = PostModel.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, template_name='blog_details.html', context=context)
"""
# Blog detail cbv
class BlogDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel
    context_object_name = 'post'