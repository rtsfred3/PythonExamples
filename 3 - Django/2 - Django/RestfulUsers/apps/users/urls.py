from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>/', views.user, name='user'),
    path('<int:num>/edit', views.user_edit, name='user_edit'),
    path('<int:num>/destroy', views.user_delete, name='user_delete'),
    path('new', views.user_new, name='user_new'),
    path('create', views.user_create, name='user_create'),
    path('update', views.user_update, name='user_update'),
]