from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, "users/profile.html") # id görmke için ekledik bnu

def index(request):
    return render(request, "index.html", {"user": request.user})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')  # Kayıttan sonra anasayfaya yönlendirme
    else:
        form = UserRegisterForm()
    
    return render(request, "users/register.html", {"form": form})
