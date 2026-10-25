from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, welcome to the Educare home page!")
def about(request):
    a = 50+70
    return HttpResponse(f"The result of the addition is: {a}")
