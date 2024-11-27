from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Jersey(request):
    return HttpResponse('<h1>Orange is the Jersey colour of PBkS</h1>')

def owner(request):
    return HttpResponse('<h1>Preety Zinta is the owner of PBKS</h1>')