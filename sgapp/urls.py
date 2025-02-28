from django.urls import path
from sgapp import views

urlpatterns =[
    path("",views.index,name="index"),
]


