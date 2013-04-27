from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from blog.forms import BlogEntryForm
from blog.models import BlogEntry

def entries(request):
    entries = BlogEntry.objects.all()
    return render_to_response("blog/entries.html", {'entries': entries})

@login_required
def entry_create(request):
    form = BlogEntryForm()
    if request.method == "POST":
        form = BlogEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('entries'))
    return render(request, "blog/entry_create.html", {'form': form})
