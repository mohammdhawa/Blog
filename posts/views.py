from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment


def post_list(request):                                     
    posts = Post.objects.all()                              
    
    context = {                                             
        'object_list': posts, 
               }
    return render(request, 'posts/post_list.html', context) 



def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'posts/post_detail.html', context)






from .forms import PostForm

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
    
    return render(request, 'posts/new.html', context)


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
    
    return render(request, 'posts/edit.html', context)



def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('/posts/')

    context = {'object': post}
    return render(request, 'posts/post_confirm_delete.html', context)

