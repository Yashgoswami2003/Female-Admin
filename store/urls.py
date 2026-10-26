from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('secure-login/', views.custom_admin_login, name='secure_login'),
    path('make-admin/', views.create_admin_user, name='make_admin'),
]