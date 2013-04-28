from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^entries/$', 'blog.views.entries', name='entries'),
    url(r'^entry/create/$', 'blog.views.entry_create', name='entry_create'),
    url(r'^entries/(?P<page>\d+)/$', 'blog.views.entries_page', name='entries_page')
)
