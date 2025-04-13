from django.db import models
from django.contrib.auth.models import AbstractUser

# 🔹 Özel kullanıcı modelin
class User(AbstractUser):
    ROLE_CHOICES = (
        ('normal', 'Normal Kullanıcı'),
        ('gurme', 'Gurme'),
        ('moderator', 'Moderatör'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='normal')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.username


# 🔹 Yorum modeli
class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=255)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Bekliyor'),
        ('approved', 'Onaylandı'),
        ('rejected', 'Reddedildi')
    ], default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.restaurant_name} - {self.rating}"


# 🔹 Gurme başvurusu modeli
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application_text = models.TextField(verbose_name="Başvuru Metni")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Beklemede'),
        ('approved', 'Onaylandı'),
        ('rejected', 'Reddedildi')
    ], default='pending')

    def __str__(self):
        return f"{self.user.username} başvurdu ({self.status})"
