from django.urls import path

from posts.views import ( create_post, edit_post, 
                         delete_post, post_list, 
                         post_detail)

from posts.api import PostListAPI, PostDetailAPI


urlpatterns = [
    path('posts/', post_list, name='posts'),
    # path('posts/', PostList.as_view(), name='posts'),
    path('posts/<int:pk>', post_detail, name='post_detail'),
    # path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('posts/create/', create_post, name='create_post'),
    # path('posts/create/', AddPost.as_view(), name='create_post'),
    path('posts/<int:pk>/edit', edit_post, name='edit_post'),
    # path('posts/<int:pk>/edit', EditPost.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete', delete_post, name='delete_post'),
    # path('posts/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),


    path('posts/api', PostListAPI.as_view(), name='post_api'),
    path('posts/api/<int:pk>/', PostDetailAPI.as_view(), name='api_detail'),
]
