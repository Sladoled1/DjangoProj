from django.db import models

# Create your models here.
class Car(models.Model):
    CarModel=models.CharField(max_length=60)
    CarDescription=models.TextField(null=True,blank=True)
    CarColor=models.TextField(null=True,blank=True,max_length=30)
    CarYear=models.IntegerField(null=True,blank=True)
    CarImage=models.ImageField(null=True,blank=True)
    RentPrice=models.IntegerField()
    CarUsing=models.BooleanField()
    UserRentId=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.CarModel

    def ChangeRent(self,Userid):
        if self.CarUsing == False:
            self.CarUsing = True
            self.UserRentId = Userid

    def StopRent(self):
        if self.CarUsing == True:
            self.CarUsing = False
            self.UserRentId = None