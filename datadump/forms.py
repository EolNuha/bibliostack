from django import forms
from .models import Post
from taggit.forms import TagField


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'image']
    tags = TagField(help_text="Add up to 5 tags that most describe what your question is about")
