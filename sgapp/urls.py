from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .views import (
    index,
    register,
    login_redirect_view,
    moderator_panel,
    gurme_dashboard,
    home_view
)

urlpatterns = [
    path('', index, name='index'),  # Açılış sayfası
    path('register/', register, name='register'),  # Kayıt
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('yorumlar/', views.yorumlar_view, name='yorumlar'),  # 💥 Burası önemli!
    path('restoranlar/', views.restoranlar_view, name='restoranlar'),  # bu satır önemli
    path('gurme-basvuru/', views.gurme_basvuru_view, name='gurme_basvuru'),
    path('home/', views.home_view, name='home'),


    path('redirect-login/', login_redirect_view, name='login_redirect'),  # Giriş sonrası yönlendirme

    # Dashboardlar
    path('moderator/', moderator_panel, name='moderator_panel'),
    path('gurme/', gurme_dashboard, name='gurme_dashboard'),
    path('home/', home_view, name='home'),  # Normal kullanıcı paneli
]
