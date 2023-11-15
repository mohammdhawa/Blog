from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from posts.views import PostList, PostDetail, create_post, edit_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    # path('posts/', post_list, name='posts'),
    path('posts/', PostList.as_view(), name='posts'),
    # path('posts/<int:pk>', post_detail, name='post_detail'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:pk>/edit', edit_post, name='edit_post'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)