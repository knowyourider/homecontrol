from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skylight.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^skylight/', include('skylight.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
