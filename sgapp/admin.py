from django.contrib import admin
from .models import User

admin.site.register(User)

from .models import Review
admin.site.register(Review)
from .models import Review, User, Application


admin.site.register(Application)
# sgapp/admin.py

from django.contrib import admin
from .models import Restaurant

admin.site.register(Restaurant)
