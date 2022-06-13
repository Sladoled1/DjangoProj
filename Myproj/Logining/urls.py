from django.urls import path
from django.contrib import admin
from .  import views
from django.http import HttpResponse




urlpatterns = [
    path('',views.home, name="home" ),
    path('home/', views.home, name="home"),
    path('admin/',admin.site.urls ),
    path('logg/', views.logg, name="logging"),

]