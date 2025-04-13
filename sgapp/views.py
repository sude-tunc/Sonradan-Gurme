from .models import Application

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

def yorumlar_view(request):
    return render(request, 'yorumlar.html')

def restoranlar_view(request):
    return render(request, 'restoranlar.html')  # restoranlar.html senin sayfa dosyanın ismi olacak

def gurme_basvuru_view(request):
    return render(request, 'gurme_basvuru.html')

from .models import Review  # Model adın buysa
from django.shortcuts import render



from .models import Review

def yorumlar_view(request):
    yorumlar = Review.objects.filter(status='approved').order_by('-created_at')
    return render(request, 'yorumlar.html', {'yorumlar': yorumlar})



def basvuru_inceleme_view(request):
    basvurular = Application.objects.filter(status='pending')
    return render(request, 'basvuru_inceleme.html', {'basvurular': basvurular})

def yorum_inceleme_view(request):
    yorumlar = Review.objects.filter(status='pending')
    return render(request, 'yorum_inceleme.html', {'yorumlar': yorumlar})

def yorum_ekle_view(request):
    # form logic burada olacak
    return render(request, 'yorum_ekle.html')

from django.shortcuts import render, redirect
from .models import Review

def yorum_ekle_view(request):
    if request.method == 'POST':
        restoran = request.POST.get('restaurant_name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            user=request.user,
            restaurant_name=restoran,
            rating=rating,
            comment=comment,
            status='pending'
        )
        return redirect('home')  # veya nereye yönlendirmek istersen

    return render(request, 'yorum_ekle.html')



