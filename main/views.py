from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.

def home_view(request,*args,**kwargs):
    print(request.user)
    #return HttpResponse("<h1>Test website please ignore </h1>");
    return render(request,"home.html",{})

def bigshaq(request,*args,**kwargs):
    print(request.user)
    return render(request,"bigshaq.html",{})


def projects_view(request,*args,**kwargs):
    print(request.user)
    return render(request,"projects.html",{})


