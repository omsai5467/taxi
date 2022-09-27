from django.contrib import admin

# Register your models here.

from  .models import cars,CustomerInformation
admin.site.register(cars)
admin.site.register(CustomerInformation)
# admin.site.register(Taxibooking)