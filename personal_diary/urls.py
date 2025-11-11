# INF 601 - Advanced Python
# Illia Ivanov
# Mini Project 4

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from journal import views as journal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journal.urls')),
    
    # Authentication URLs
    path('register/', journal_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]