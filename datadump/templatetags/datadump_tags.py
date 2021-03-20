from django import template
from datadump.models import Post

register = template.Library()


def get_latest_posts(arg):
    value = Post.objects.all()[:arg]
    return value


def get_most_tags(arg):
    value = Post.tags.most_common()[:arg]
    return value


def get_most_comments(arg):
    post_list = Post.objects.all().order_by('-comments')
    post_counter = {}
    for post in post_list:
        if post in post_counter:
            post_counter[post] += 1
        else:
            post_counter[post] = 1
    popular_posts = sorted(post_counter, key=post_counter.get, reverse=True)
    top = popular_posts[:arg]
    return top


register.filter('get_latest_posts', get_latest_posts)
register.filter('get_most_tags', get_most_tags)
register.filter('get_most_comments', get_most_comments)