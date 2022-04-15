from django.shortcuts import render
from .models import Post,Tag,Comment
from django.views.generic import ListView,View

# Create your views here.
class PostsView(ListView):
    template_name = "resumeapp/blog.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


def post_detail(request, slug):
    post = Post.objects.get(slug = slug)

    return render(request, "resumeapp/single-blog.html", {
        'post':post,
        'tagss':Tag.objects.all(),
        'comments': post.comments.all(),
    })
