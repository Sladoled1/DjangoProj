from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'Logining/home.html')

def logg(request):
    return render(request,'Logining/logg.html')