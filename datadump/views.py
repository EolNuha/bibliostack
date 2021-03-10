from django.shortcuts import render
from django.core.paginator import Paginator


def home(response):
    return render(response, 'datadump/index.html', {})


def posts(response, page):
    posts = []
    paginator = Paginator(posts, 5)
    page_number = page
    page_obj = paginator.get_page(page_number)

    return render(response, 'pagination.html', {'page_obj': page_obj})

def post_details(request):
    posts = Post.objects.all()
    form = PostForm()
    context = {
        'form' : form,
        'posts': posts

    }
    return render(request, 'datadump/details.html', context)
