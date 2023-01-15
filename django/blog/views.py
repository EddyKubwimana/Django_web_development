from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.4

def Home(request):
    return HttpResponse('<h1>Home</h1>')

def News(request):
    return HttpResponse('<h1>News</h1>')
def Published(request):
    return HttpResponse('<h1>Published papers</h1>')
def Editors(request):
    return HttpResponse('<h1> Editors</h1>')
def About(request):
    return HttpResponse('<h1>About</h1>')




