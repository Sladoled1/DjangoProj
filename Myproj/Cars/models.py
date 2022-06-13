from django.db import models

# Create your models here.
class Car(models.Model):
    CarModel=models.CharField(max_length=60)
    CarDescription=models.TextField(null=True,blank=True)
    CarColor=models.TextField(null=True,blank=True,max_length=30)
    CarYear=models.IntegerField(null=True,blank=True,max_length=30)
    RentPrice=models.IntegerField()
    CarUsing=models.BooleanField()

    def __str__(self):
        return self.CarModel