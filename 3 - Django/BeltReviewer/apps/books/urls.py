from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.book, name='book'),
    
    path('add', views.add, name='add'),
    path('create', views.create, name='create'),
]