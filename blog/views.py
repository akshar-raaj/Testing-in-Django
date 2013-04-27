from blog.models import BlogEntry
from django.shortcuts import render, render_to_response

def entries(request):
    entries = BlogEntry.objects.all()
    return render_to_response("blog/entries.html", {'entries': entries})
