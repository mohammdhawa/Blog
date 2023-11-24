from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment

from .forms import PostForm, CommentForm


def post_list(request):                                     
    posts = Post.objects.all()                              
    
    context = {                                             
        'object_list': posts, 
               }
    return render(request, 'posts/post_list.html', context) 



def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = post
            myform.save()
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'posts/post_detail.html', context)



def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm()

    context = {'form': form}
    
    return render(request, 'posts/post_form.html', context)


def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm(instance=post)

    context = {'form': form}
    
    return render(request, 'posts/post_form.html', context)



def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('/posts/')

    context = {'object': post}
    return render(request, 'posts/post_confirm_delete.html', context)






    