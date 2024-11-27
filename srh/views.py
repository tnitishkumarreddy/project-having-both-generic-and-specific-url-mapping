from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def batsmens(request):
    return HttpResponse('<h1>The main batsmen in the SRH team are Head,Abhishek,Klassen,Ishan,Nitish</h1>')

def bowlers(request):
    return HttpResponse('<h1>The main bowlers in the srh team are Shami,cummins,Zampa,rahul Chahar and Unadkat</h1>')