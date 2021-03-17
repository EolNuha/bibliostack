from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag


def post_list(request, tag_slug=None):
    posts = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    context = {
        'posts': posts,
        'tag':tag,
    }
    return render(request, 'datadump/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='active',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'datadump/post/detail.html', context)
