from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_details, name="posts"),
    path('posts/<int:page>', views.posts),

]