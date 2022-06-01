from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    return HttpResponse("my account.")

def myPage(request,idNumber):
    return HttpResponse("my account.")

def logIn(request):
    return HttpResponse("log in.")