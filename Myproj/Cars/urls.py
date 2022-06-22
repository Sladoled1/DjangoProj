from django.urls import path
from .  import views

urlpatterns = [
    path('result/', views.result,name="result"),
    path('rent/<str:pk>/', views.rent,name="rent"),
    path('usingcar/' ,views.UsingCar,name="using"),
]
#python manage.py runserver