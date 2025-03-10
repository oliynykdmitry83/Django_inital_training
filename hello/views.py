from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request, "hello/index.html")

def dimi(request):
    return HttpResponse("Hello, Dimi!")

def nat(request):
    return HttpResponse("Hello, Natalia!")

def greet(request,  name):
    return render(request, "hello/greet.html", {
       "name" : name.capitalize()
    })