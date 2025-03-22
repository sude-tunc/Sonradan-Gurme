from django.urls import path
from django.contrib.auth.views import LoginView
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

    path('redirect-login/', login_redirect_view, name='login_redirect'),  # Giriş sonrası yönlendirme

    # Dashboardlar
    path('moderator/', moderator_panel, name='moderator_panel'),
    path('gurme/', gurme_dashboard, name='gurme_dashboard'),
    path('home/', home_view, name='home'),  # Normal kullanıcı paneli
]
