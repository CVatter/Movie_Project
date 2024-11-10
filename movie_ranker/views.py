#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello World! This is the home page.")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("This is the abaout page!")
    return render(request, 'about.html')

