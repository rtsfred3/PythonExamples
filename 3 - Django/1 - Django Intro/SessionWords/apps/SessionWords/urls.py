from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'process$', views.process, name='process'),
    re_path(r'destroy$', views.destroy, name='destroy'),
]