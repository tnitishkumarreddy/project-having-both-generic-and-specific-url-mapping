from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def captain(request):
    return HttpResponse('<h1>Rishab Pant is the captain of LSG</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>Pooran is the Vice-captain of LSG</h1>')