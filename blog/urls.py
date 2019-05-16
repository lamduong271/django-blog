from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.list, name="blog"),
    path('<int:id>/', views.post, name="post")
]
