from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home(request):
    # return HttpResponse("Welcome to Aquarium store Homepage")
    return render(request, "home.html")