from django.shortcuts import render

# Create your views here.
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts, 
               }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post
    }

    return render(request, 'posts/post_details.html', context)