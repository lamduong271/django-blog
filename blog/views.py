from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
# from .models import Post
# from django.views.generic import ListView, DetailView
# Create your views here.

# class PostListView(ListView):
#     queryset = Post.objects.all().order_by("-date")
#     template_name = 'blog/blog.html'
#     context_object_name = 'Posts' # Posts in blog.html
#     paginate_by = 1
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post.html'
# def post(request,id):
#     post = Post.objects.get(id=id)
#     return render(request,'blog/post.html',{'post':post})

def post(request,pk):
    post = get_object_or_404(Post, pk=pk) #when post not found retuen 404
    form = CommentForm()
    print(request.method)
    if request.method == 'POST':
        form = CommentForm(request.POST, author = request.user,post=post)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'blog/post.html',{'post': post, 'form':form})


