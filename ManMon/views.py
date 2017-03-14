from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def callMainPage(request):
    return HttpResponse("Hello, this is ManMon app")

