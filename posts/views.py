from django.shortcuts import render, redirect

# Create your views here.
from .models import Post

"""
def post_list(request):                                     : query
    posts = Post.objects.all()                              
    
    context = {                                             : context
        'posts': posts, 
               }
    return render(request, 'posts/post_list.html', context) : template
"""

from django.views.generic import ListView

class PostList(ListView):       # context: model_list / bject_list
    model = Post                # template: model_action = post_list 


"""
def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post
    }

    return render(request, 'posts/post_details.html', context)
"""

from django.views.generic import DetailView

class PostDetail(DetailView):           # context: post, object
    model = Post                        # template: post_detail



from .forms import PostForm

def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
    else:
        form = PostForm()

    context = {'form': form}
    
    return render(request, 'posts/new.html', context)