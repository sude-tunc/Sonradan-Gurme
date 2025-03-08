"""
URL configuration for SnrdnGrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from sgapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("sgapp/", include('sgapp.urls')),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path('accounts/', include('django.contrib.auth.urls')),  # For built-in auth views
    path('register/', views.register, name='register'),  
    path('profile/', views.profile, name='profile'),  # Profile page view
    path('welcome/', views.welcome, name='welcome'),  # Welcome page view
    path('', views.main_page, name='main_page'),  # Main page URL pattern
    path('login/', views.custom_login, name='login'),  # Custom login view
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
