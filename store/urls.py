from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vlogs/', views.vlog_list, name='vlog_list'),
]