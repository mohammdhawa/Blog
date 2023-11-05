from django.db import models

# Used moduels
from django.utils import timezone
from taggit.managers import TaggableManager

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
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    # publish_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(auto_now=True)

    tags = TaggableManager()
    image = models.ImageField(upload_to='post')


    def __str__(self) -> str:
        return self.title