from django.contrib import admin

# kayıt modelleri burada!!!!!

from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')  # id leri d listeye ekledik burda, başka şeleri d ekleyebilirz

admin.site.unregister(User)  # hahazır olan user modeilini çıkardık
admin.site.register(User, UserAdmin)  # snr kedni yaptığımız halini ekledik, tkr değiştiirirksek buraya bak
