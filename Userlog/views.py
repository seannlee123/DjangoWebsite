from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is test page")

def welcome(request):
    return HttpResponse("Hello welcome to the page")