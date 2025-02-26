from django import forms
from django.contrib.auth.models import User

#######################################REGİSTER KISMI#########################################

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'çalınamicak bi şifre gir'}),  
        label="sifren ne"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'tkr gir şu şifreyi'}),  
        label="şifreni LÜTFEN tkr gir"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'nick in ne olsun',
            'email': 'mail ini yaz',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'unique nick yaz'}),
            'email': forms.EmailInput(attrs={'placeholder': 'kullandıın maili yaz'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            self.add_error('password_confirm', "Salak, şifreler eşleşmiyor!")


###############################LOGİN KISMI############################################
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Kkullanıcı adını giriver'}),
        label="nick"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'şifreni girirvenr'}),
        label="sifre"
    )

