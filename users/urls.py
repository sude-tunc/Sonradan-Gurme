from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register
from .forms import UserLoginForm  # Login formunu içe aktarıyoruz

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html", authentication_form=UserLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
