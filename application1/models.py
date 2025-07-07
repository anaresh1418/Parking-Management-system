from django.db import models
from datetime import datetime

# Create your models here.
class add_category(models.Model):
    parkingareanumber=models.CharField(max_length=100)
    vehicletype=models.CharField(max_length=100)
    vehiclelimit=models.IntegerField()
    parkingharge=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.BooleanField(default=True)
    doc=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return  self.vehicletype

class add_vehicle(models.Model):
    vehicle_no=models.CharField(max_length=250)
    parkingareanumber = models.ForeignKey(add_category,on_delete=models.CASCADE)
    vehicletype=models.CharField(max_length=200)
    parkingharge=models.DecimalField(max_digits=10,decimal_places=2)
    status = models.BooleanField(default=True)
    arrival_time=models.DateTimeField(default=datetime.now)
