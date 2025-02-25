from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.process, name='process/'),
    path('process', views.process, name='process'),
    path('result/', views.result, name='result/'),
    path('result', views.result, name='result'),
]