from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from taggit.models import Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.defaultfilters import slugify
from .forms import CreatePost
from django.db.models.signals import pre_save
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


def post_list(request, tag_slug=None):
    object_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        if 'contact_us' in request.POST:
            name = request.POST.get('first')
            last_name = request.POST.get('last')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            html_mail = f'<h5>Phone: {phone}<br>Email: {email}</h5><p>{message}</p>'
            subject, from_email, to = name + " " + last_name, email, 'eol.nuha22@gmail.com'
            msg = EmailMessage(subject, html_mail, from_email, [to])
            msg.content_subtype = "html"
            msg.send()

    context = {
        'page': page,
        'posts': posts,
        'tag': tag,
        'all_posts': Post.objects.all(),
    }
    return render(request, 'datadump/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        if 'contact_us' in request.POST:
            name = request.POST.get('first')
            last_name = request.POST.get('last')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            html_mail = f'<h5>Phone: {phone}<br>Email: {email}</h5><p>{message}</p>'
            subject, from_email, to = name + " " + last_name, email, 'eol.nuha22@gmail.com'
            msg = EmailMessage(subject, html_mail, from_email, [to])
            msg.content_subtype = "html"
            msg.send()

        elif 'add_comment' in request.POST:
            if request.user.is_authenticated:
                name = request.user.username
                email = request.user.email
                comment = request.POST.get('comment')
                c = Comment(post=post, name=name, email=email, body=comment)
                c.save()
            else:
                name = request.POST.get('name')
                email = request.POST.get('email')
                comment = request.POST.get('comment')
                c = Comment(post=post, name=name, email=email, body=comment)
                c.save()
    context = {
        'post': post,
        'comments': comments,
        'all_posts': Post.objects.all(),
    }
    return render(request, 'datadump/post/detail.html', context)


@login_required
def create_post(request):
    create_form = []
    if request.method == 'POST':
        if 'contact_us' in request.POST:
            name = request.POST.get('first')
            last_name = request.POST.get('last')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            html_mail = f'<h5>Phone: {phone}<br>Email: {email}</h5><p>{message}</p>'
            subject, from_email, to = name + " " + last_name, email, 'eol.nuha22@gmail.com'
            msg = EmailMessage(subject, html_mail, from_email, [to])
            msg.content_subtype = "html"
            msg.send()
        elif 'create_post' in request.POST:
            create_form = CreatePost(request.POST)
            if create_form.is_valid():
                def pre_save_post_receiver(sender, instance, *args, **kwargs):
                    instance.slug = slugify(instance.title)
                    instance.author = request.user
                    instance.status = "published"
                pre_save.connect(pre_save_post_receiver, sender=Post)
                create_form.save()
                return redirect('/datadump')
    else:
        create_form = CreatePost()

    context = {
        'create_form': create_form,
        'all_posts': Post.objects.all(),
    }
    return render(request, 'datadump/post/create_post.html', context)


def search_posts(request):
    search = request.GET.get('search')
    vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
    query = SearchQuery(search)
    search_results = Post.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.3).order_by('-rank')
    paginator = Paginator(search_results, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'search': search,
        'page': page,
        'posts': posts,
        'search_results': search_results,
        'all_posts': Post.objects.all(),
    }
    return render(request, 'datadump/post/search_results.html', context)
