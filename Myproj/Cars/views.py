from django.shortcuts import render,redirect
from .models import Car

# Create your views here.
def rent(request,pk):
    car = None
    cars = Car.objects.all()
    if request.method == 'POST':
        for j in cars:
            if j.UserRentId == request.user.id:
                return redirect('using')
            else:
                rentcar= Car.objects.get(id=int(pk))
                rentcar.ChangeRent(request.user.id)
                rentcar.save()
                return redirect('result')

    for i in cars:
        if i.id== int(pk):
            car=i
    context = {'car': car}

    return render(request, 'Cars/rent.html', context)

def result(request):
    cars=Car.objects.all()
    context={'cars':cars}
    return render(request,'Cars/result.html',context)

def UsingCar(request):
    if request.method == 'POST':
        stoprent= Car.objects.get(CarUsing=request.user.id)
        stoprent.StopRent()
        stoprent.save()
        return redirect('using')
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'Cars/using.html', context)