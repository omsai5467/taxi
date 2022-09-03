from django.db import models

# Create your models here.



# name/
# email
# time/
# car

class cars(models.Model):
    nameOfCar =     models.CharField(max_length=255, blank=True)
    carId =     models.CharField(max_length=255, blank=True)
    carImg =     models.ImageField(upload_to="static/car/images")
    createdAT = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nameOfCar



class CustomerInformation(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phoneNumber = models.CharField(max_length=255, blank=True)
    createdAT = models.DateTimeField(auto_now_add=True)
    BookedCarID = models.CharField(max_length=255, blank=True)
    