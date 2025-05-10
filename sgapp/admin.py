from django.contrib import admin
from .models import User, Review, Application, Restaurant

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')  # Admin paneli sütunları
    search_fields = ('name', 'address')  # Arama alanı
    ordering = ('name',)  # Alfabetik sıralama
