from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('city_home/', views.city_home, name='city_home'),
    path('', views.city_list, name='city_list'),
    path('details/<int:id>', views.details, name='details'),
]