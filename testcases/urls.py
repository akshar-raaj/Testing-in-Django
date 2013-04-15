from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^testcases/', include('testcases.foo.urls')),
    url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
