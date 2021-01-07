from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.success, name='success'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logoff', views.logoff, name='logoff'),
    path('users/<int:num>', views.user, name='user'),
    
    path('quotes', views.quotes, name='quotes'),
    path('likes', views.likes, name='likes'),
    path('submit_quote', views.submit_quote, name='submit_quote'),
    path('delete_quote', views.delete_quote, name='delete_quote'),
    
    path('myaccount/<int:num>', views.myaccount, name='myaccount'),
    path('edit_user', views.edit_user, name='edit_user'),
]