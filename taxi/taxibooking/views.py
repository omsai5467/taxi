from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from .models import cars ,CustomerInformation,Taxibooking
from django.http import JsonResponse
from django.core import serializers
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = cars
        fields = '__all__'


# Create your views here.

def home(request):
    x = cars.objects.all()
    return  render(request, 'index.html',{"data":x})



def get(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    return response_data

@csrf_exempt
def getcar_details(request):
    try:
        if(request.method == "POST"):
            data = JSONParser().parse(request)
            print(data["fromAdress"])
            data = cars.objects.all().filter(cartype = data["cartype"])
            res = CarSerializer(data,many=True)
            return  JsonResponse({'data': res.data})
    except Exception as e:
        print(e)
        return JsonResponse({"msg":"fuck you"})



@csrf_exempt
def bookcar(request):
    try:
        if(request.method == "POST"):
            data = JSONParser().parse(request)
            print(1)
            name = data["name"]
            print(2)
            phone = data["phone"]
            print(3)
            email = data["email"]
            print(4)
            bookedCarID = data["bookedCarID"]
            print(5)
            fromAdress = data["fromAdress"]
            print(6)
            toAdress = data["toAdress"]
            print(7)
            
            time = data["time"]
            print(8)
        
            date = data["date"]
            print(9)
           
            re = data["return"]
            print(10)
            res = {
                "status":"200"
            }
            print(11)
            obj = CustomerInformation()
            print(12)
            obj.name = name
            print(13)
            obj.phone = phone  
            print(14)
            obj.email = email
            print(15)
            obj.bookedCarID = bookedCarID
            obj.save()
            print(16)
            print(17)
            print(18)
            obj = Taxibooking()
            print(19)

            obj.fromAdress = fromAdress
            print(20)
            obj.toAdress = toAdress
            print(21)
            obj.time = time
            print(22)
            obj.date = date
            print(23)
            obj.hereturn = re
            print(24)
            obj.custmerid = "8"
            print(25)
            obj.save()
            print(26)
            print(27)
            print(28)
            return  JsonResponse({'data': res})
    except :
        return JsonResponse({"msg":"fuck you"})

