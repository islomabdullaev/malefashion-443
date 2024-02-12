from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from blogs.forms import CommentForm

from blogs.models import CommentModel, PostModel
from django.views.generic import DetailView, CreateView

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


def create_comment(request, pk):
    current_url_path = request.META['HTTP_REFERER']
    if request.method == "POST":
        post = PostModel.objects.get(pk=pk)
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comments = request.POST.get("comments")
        CommentModel.objects.create(
            post=post,
            name=name,
            email=email,
            phone=phone,
            comments=comments
        )

        return redirect(current_url_path)