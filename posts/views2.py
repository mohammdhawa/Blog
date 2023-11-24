from .models import Post



from django.views.generic import ListView

class PostList(ListView):       # context: model_list / bject_list
    model = Post                # template: model_action = post_list 



from django.views.generic import DetailView

class PostDetail(DetailView):           # context: post, object
    model = Post                        # template: post_detail




from django.views.generic import UpdateView, CreateView, DeleteView

class AddPost(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'



class EditPost(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'



class DeletePost(DeleteView):
    model = Post
    success_url = '/posts/'