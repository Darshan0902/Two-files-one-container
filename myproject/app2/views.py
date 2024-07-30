import requests
from django.http import JsonResponse
from django.shortcuts import render

def get_data():
    response = requests.get('http://app1:8000/')
    return response.json()

def page2(request):
    data = {
          get_data()
    }
    return JsonResponse(data)
docker.host.internal