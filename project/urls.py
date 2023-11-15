from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from posts.views import post_list, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_list, name='posts'),
    path('posts/<int:pk>', post_detail, name='post_detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)