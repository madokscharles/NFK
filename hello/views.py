from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def madoks(request):
    return HttpResponse("Hello, Madoks!")

def ben(request):
    return HttpResponse("Hello, Ben!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })