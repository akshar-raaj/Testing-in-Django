from django.forms import ModelForm

from blog.models import BlogEntry

class BlogEntryForm(ModelForm):
    class Meta:
        model = BlogEntry
