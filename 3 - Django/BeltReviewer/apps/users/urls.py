from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.success, name='success'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logoff', views.logoff, name='logoff'),
    
    path('users/<int:num>', views.user, name='user'),
]