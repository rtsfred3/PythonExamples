from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logoff', views.logoff, name='logoff'),
    
    path('wall/', views.wall, name='wall'),
    path('post_message', views.post_message, name='post_message'),
    path('post_comment', views.post_comment, name='post_comment'),
]