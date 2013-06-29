from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.http import Http404

from .forms import BlogEntryForm
from .models import BlogEntry


def entries(request):
    entries = BlogEntry.published.all()
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


def entries_page(request, page):
    page = int(page)
    entries = BlogEntry.published.all()
    paginator = Paginator(entries, 10)  # 10 entries per page
    if page > paginator.num_pages:
        raise Http404()
    page_ = paginator.page(page)
    object_list = page_.object_list
    return render(request, "blog/entries_page.html", {"entries": object_list})
