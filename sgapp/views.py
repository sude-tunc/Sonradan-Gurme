from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def index(request):
    my_dict = {'insert_me': "YENİ YEMEKLER KEŞFETMEYE HAZIR MISIN!!"}
    return render(request, 'index.html', context=my_dict)

def main_page(request):
    return render(request, 'main_page.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})