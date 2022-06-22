from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def loginPage(request):
    page='login'
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            pass
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
    context={'page' : page}
    return render(request, 'Logining/logg.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def RegisterUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit = False)
            user.save()
            return redirect('home')
    return render(request,'Logining/logg.html',{'form':form})