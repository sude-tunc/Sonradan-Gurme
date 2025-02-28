from django import forms
from django.contrib.auth.models import User

#######################################REGİSTER KISMI#########################################

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Çalınmayacak bir şifre girin'}),  
        label="şifre:"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Tekrar gir'}),  
        label="şifre(tekrar):"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'nick:',
            'email': 'mail:',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'nick'}),
            'email': forms.EmailInput(attrs={'placeholder': 'mail'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            self.add_error('password_confirm', "Şifreler eşleşmiyor!!!!")


###############################LOGİN KISMI############################################
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'kullanıcı adını girin'}),
        label="nick"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'şifrenizi girin'}),
        label="sifre"
    )

