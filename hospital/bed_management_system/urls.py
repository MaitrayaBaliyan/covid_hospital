from django.contrib import admin
from bed_management_system import views
from django.urls import path, include

urlpatterns = [
    path('list/<str:section>/<str:status>/', views.list, name='list'),
    path('list/<str:status>/', views.list, name='list_status'),
    path('list/', views.list, name='list_all'),
    path('check_status/', views.check_status, name='check_status'),
    path('logout/', views.user_logout, name='user_logout'),
    path('discharge/', views.discharge, name='discharge'),
    path('allocatement/', views.allocatement, name='allocatement'),
    path('', views.index, name='index'),
]