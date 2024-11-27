from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>Kl Rahul is the captian of DC</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>Faf Duplesis is the Vice-captian of DC</h1>')