from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment

from django_summernote.admin import SummernoteModelAdmin



class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['title', 'draft', 'category']
    list_filter = ['draft', 'tags', 'category']
    search_fields = ['title']

admin.site.register(Post, ProductAdmin)

admin.site.register(Category)

admin.site.register(Comment)