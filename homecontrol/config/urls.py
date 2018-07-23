from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Examples:
    # url(r'^$', 'skylight.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('skylight/', include('skylight.urls')),
    path('admin/',  admin.site.urls),
]
