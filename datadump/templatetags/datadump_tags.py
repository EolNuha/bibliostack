from django import template
from django.db.models import Count
from datadump.models import Post
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()


@register.simple_tag
def get_latest_posts(count=5):
    return Post.published.all()[:count]


@register.simple_tag
def get_most_tags(count=5):
    return Post.tags.most_common()[:count]


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.md_in_html'])
