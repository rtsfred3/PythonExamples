from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:year>/', views.year, name='year'),
    path('<int:year>/edit/', views.yearedit, name='yearedit'),
    path('<int:year>/delete/', views.yeardelete, name='yeardelete'),
]