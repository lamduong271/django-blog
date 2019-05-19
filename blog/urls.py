from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from .models import Post

# urlpatterns = [
#     path('', views.PostListView.as_view(), name="blog"),
#     path('<int:pk>/', views.PostDetailView.as_view(), name="post")
# ]
urlpatterns = [
    path('', ListView.as_view(
        queryset = Post.objects.all().order_by("-date"),
        template_name = 'blog/blog.html',
        context_object_name = 'Posts', # Posts in blog.html
        paginate_by = 1,
        ), name="blog"),
    path('<int:pk>/', DetailView.as_view(
         model = Post,
        template_name = 'blog/post.html',
    ), name="post")
]
