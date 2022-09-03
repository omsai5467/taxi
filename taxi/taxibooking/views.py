from django.shortcuts import render
import json
from django.http import HttpResponse



# Create your views here.

def home(request):
    return  render(request, 'index.html')



def get(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    return response_data