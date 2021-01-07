from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogindex, name='blogindex'),
    path('new/', views.blognew, name='blognew'),
    path('create/', views.blogcreate, name='blogcreate'),
    path('<int:num>/', views.blogview, name='blogview'),
    path('<int:num>/edit/', views.blogedit, name='blogedit'),
    path('<int:num>/delete/', views.blogdelete, name='blogdelete'),
]