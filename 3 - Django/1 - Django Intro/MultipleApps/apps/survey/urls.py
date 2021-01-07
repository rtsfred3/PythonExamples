from django.urls import path

from . import views

urlpatterns = [
    path('', views.surveyindex, name='surveyindex'),
    path('new/', views.surveynew, name='surveynew'),
]