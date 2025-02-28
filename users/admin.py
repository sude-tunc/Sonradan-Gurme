from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')  # ID'yi listeye ekledik

admin.site.unregister(User)  # Önce User modelini çıkar
admin.site.register(User, UserAdmin)  # Sonra kendi düzenlediğimiz haliyle tekrar ekle
