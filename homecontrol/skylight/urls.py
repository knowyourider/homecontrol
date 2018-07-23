from django.urls import path

from . import views

app_name = "skylight"

urlpatterns = [
    path('', views.index, name='index'),
    # url(r'^control/$', views.ControlView.as_view(), name='control'),
    path('control/', views.ControlView.as_view(), name='control'),
]
