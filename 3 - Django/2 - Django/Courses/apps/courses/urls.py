from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('destroy/<int:num>', views.destroy, name='destroy'),
    path('destroy_course', views.destroy_course, name='destroy_course'),
]