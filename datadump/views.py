from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import PostForm


def posts(response, page):
    object_models = []
    paginator = Paginator(object_models, 5)
    page_number = page
    page_obj = paginator.get_page(page_number)

    return render(response, 'pagination.html', {'page_obj': page_obj})

def post_details(request):
    object_models = Post.objects.all()
    form = PostForm()
    context = {
        'form': form,
        'posts': object_models

    }
    return render(request, 'datadump/details.html', context)
