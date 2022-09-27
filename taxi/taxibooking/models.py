from django.db import models


class cars(models.Model):
    nameOfCar =     models.CharField(max_length=255, blank=True)
    carId =     models.CharField(max_length=255, blank=True)
    carImg =     models.ImageField(upload_to="static/car/images")
    createdAT = models.DateTimeField(auto_now_add=True)
    cartype = models.CharField(max_length=255, blank=True)
    priceperday = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=255, blank=True)
    milage = models.CharField(max_length=255, blank=True)
    geartype = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.nameOfCar



class CustomerInformation(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    createdAT = models.DateTimeField(auto_now_add=True)
    bookedCarID = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name



class Taxibooking(models.Model):
    fromAdress = models.CharField(max_length=255, blank=True) 
    toAdress = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    time = models.CharField(max_length=255, blank=True)
    BookedDate  = models.CharField(max_length=255, blank=True)
    BookedTime= models.CharField(max_length=255, blank=True)
    carId= models.CharField(max_length=255, blank=True)
    custmerid  =     models.CharField(max_length=255, blank=True)   
    hereturn = models.CharField(max_length=255, blank=True) 

    def __str__(self):
        return self.custmerid