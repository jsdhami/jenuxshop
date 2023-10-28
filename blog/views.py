from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse("Hello Blogy Boy")
def catagory(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse("Hello Blogy Boy's catagory")