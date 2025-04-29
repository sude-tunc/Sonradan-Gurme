from django.contrib import admin
from django.urls import path, include
from sgapp import views
from django.contrib.auth import views as auth_views

# Yeni eklediklerimiz:
from django.conf import settings
from django.conf.urls.static import static

################################## URL LERİ BURAYA DİZİYORUZ ##################################

urlpatterns = [
    path("sgapp/", include('sgapp.urls')),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('welcome/', views.welcome, name='welcome'),
    path('', views.main_page, name='main_page'),
    path('login/', views.custom_login, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('kesfet/', views.kesfet_view, name='kesfet'),
    path('restoran/<int:restoran_id>/', views.restoran_detay_view, name='restoran_detay'),
    path('restoranlar/', views.restaurant_search, name='restaurant_search'),

]

# 🌟 MEDIA dosyalarını ekle (resimler vs çalışsın diye!)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
