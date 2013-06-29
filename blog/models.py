from django.db import models
from django.contrib.auth.models import User


class PublishedBlogManager(models.Manager):
    def get_query_set(self, *args, **kwargs):
        return super(PublishedBlogManager, self).\
                get_query_set(*args, **kwargs).filter(is_published=True)


class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    is_published = models.BooleanField(default=True)
    user = models.ForeignKey(User)

    objects = models.Manager()
    published = PublishedBlogManager()
