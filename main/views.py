from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Test website please ignore </h1>");

def bigshaq(response):
    return HttpResponse("<h1>Ting goes skrrr</h1>");

