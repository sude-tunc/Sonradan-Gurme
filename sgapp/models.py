# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Kullanıcı modeli
class User(AbstractUser):
    ROLE_CHOICES = (
        ('normal', 'Normal Kullanıcı'),
        ('gurme', 'Gurme'),
        ('moderator', 'Moderatör'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='normal')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    favorite_dish = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

# 🍽 Restaurant modeli (YUKARI ALINDI)
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Alfabetik sıraya göre sıralar


# ✍️ Yorum modeli
class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    receipt = models.ImageField(upload_to='review_receipts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Bekliyor'),
        ('approved', 'Onaylandı'),
        ('rejected', 'Reddedildi')
    ], default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name} - {self.rating}"


# Gurme başvurusu modeli
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Beklemede'),
        ('approved', 'Onaylandı'),
        ('rejected', 'Reddedildi'),
    ], default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.status}"

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ModeratorFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bildirimin gönderildiği kullanıcı
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Yorum mu başvuru mu
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    decision = models.CharField(
        choices=[('approved', 'Onaylandı'), ('rejected', 'Reddedildi')],
        max_length=20
    )
    feedback_text = models.TextField(blank=True)  # Sebep
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback to {self.user.username} - {self.decision}"
