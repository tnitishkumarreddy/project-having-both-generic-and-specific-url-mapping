from django.urls import path 
from lsg.views import *

urlpatterns=[
    path('captain/',captain,name='captain'),
    path('vicecaptain/',vicecaptain,name='vicecaptain'),
]