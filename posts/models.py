from django.db import models

# Used moduels
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.

"""
    Post:
        - title
        - content
        - draft
        - author
        - image
        - tags
        - category
        - components
"""

'''
    1: HTML Widget
    2: Validation
    3: best for DB
'''


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    # publish_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.SET_NULL, null=True)

    tags = TaggableManager()
    image = models.ImageField(upload_to='post')


    def __str__(self) -> str:
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post)