# INF 601 - Advanced Python
# Illia Ivanov
# Mini Project 4

from django.urls import path
from . import views

app_name = 'journal'

urlpatterns = [
    # Home and basic pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),

    # Entry URLs
    path('entries/', views.entry_list, name='entry_list'),
    path('entry/<int:pk>/', views.entry_detail, name='entry_detail'),
    path('entry/new/', views.entry_create, name='entry_create'),
    path('entry/<int:pk>/edit/', views.entry_update, name='entry_update'),
    path('entry/<int:pk>/delete/', views.entry_delete, name='entry_delete'),

    # Task URLs
    path('entry/<int:entry_pk>/task/new/', views.task_create, name='task_create'),
    path('task/<int:task_pk>/toggle/', views.task_toggle, name='task_toggle'),
]