from django.urls import path
from . import views

app_name = 'datadump'

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('tag/<slug:tag_slug>/', views.post_list, name="post_list_tag"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/update/', views.post_update, name='post_update'),
    path('create-post/', views.create_post, name="create_post"),
    path('search/', views.search_posts, name="search_posts"),
    path('about/', views.about_us, name="about_us"),
    path('faq/', views.faq, name="faq"),
    path('team/', views.team, name="team"),
]
