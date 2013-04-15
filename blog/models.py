from django.db import models

# Create your models here.

class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    is_published = models.BooleanField(default=True)
