from django.urls import path
from .  import views
from django.http import HttpResponse




urlpatterns = [

    path('logg/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register', views.RegisterUser, name="register"),

]