from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # doğru form

# ANASAYFALAR

def index(request):
    my_dict = {'insert_me': "YENİ YEMEKLER KEŞFETMEYE HAZIR MISIN!!"}
    return render(request, 'index.html', context=my_dict)

def main_page(request):
    return render(request, 'main_page.html')

@login_required
def welcome(request):
    return render(request, 'users/welcome.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

# KAYIT (doğru form ile)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login_redirect')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# GİRİŞ
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login_redirect')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# ROL BAZLI YÖNLENDİRME
@login_required
def login_redirect_view(request):
    user = request.user
    if user.role == 'moderator':
        return redirect('moderator_panel')
    elif user.role == 'gurme':
        return redirect('gurme_dashboard')
    else:
        return redirect('home')

# DASHBOARDLAR
@login_required
def moderator_panel(request):
    return render(request, 'moderator_dashboard.html')

@login_required
def gurme_dashboard(request):
    return render(request, 'gurme_dashboard.html')

@login_required
def home_view(request):
    return render(request, 'home.html')
