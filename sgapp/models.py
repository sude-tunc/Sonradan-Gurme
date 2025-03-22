from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('normal', 'Normal Kullanıcı'),
        ('gurme', 'Gurme'),
        ('moderator', 'Moderatör'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='normal')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
