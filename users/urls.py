from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile
from .forms import UserLoginForm  # login formunu aktarioz

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html", authentication_form=UserLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("password_reset/", auth_views.PasswordResetView.as_view(
    template_name="users/password_reset.html",
    email_template_name="registration/password_reset_email.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),#mail gitti bilgilendirme sayfası
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),#yeni şifre belirleme sayfası
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),#şifre sısfırlama mesajı
    
]
