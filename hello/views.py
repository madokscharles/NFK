from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello from NFK!")

def madoks(request):
    return HttpResponse("Hello, Madoks!")

def ben(request):
    return HttpResponse("Hello, Ben!")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")