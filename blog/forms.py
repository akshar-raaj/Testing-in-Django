from django.forms import ModelForm

from .models import BlogEntry


class BlogEntryForm(ModelForm):
    class Meta:
        model = BlogEntry
