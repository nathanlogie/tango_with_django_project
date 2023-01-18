from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = "Rango says hey there partner!" + '<a href="/rango/about/">About</a>'
    return HttpResponse(response)


def about(request):
    response = "Rango says here is the about page." + '<a href="/rango/">Index</a>'
    return HttpResponse(response)
