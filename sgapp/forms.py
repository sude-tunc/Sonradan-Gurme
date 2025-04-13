from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="E-posta Adresi",
        help_text="Geçerli bir e-posta giriniz."
    )

    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,  # 💥 Eksik olan buydu!
        label="Kullanıcı Rolü"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
        labels = {
            'username': 'Kullanıcı Adı',
            'password1': 'Şifre',
            'password2': 'Şifre (Tekrar)',
            'role': 'Rol Seçiniz'
        }
        help_texts = {
            'username': '150 karakter veya daha az. Harf, rakam ve @/./+/-/_ karakterleri olabilir.',
            'password1': 'Şifren en az 8 karakter olmalı.',
            'password2': 'Aynı şifreyi tekrar girin.',
        }
        error_messages = {
            'username': {
                'unique': "Bu kullanıcı adı zaten alınmış.",
            },
        }
