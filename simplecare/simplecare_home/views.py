from django.shortcuts import render
from django.http import HttpResponse

def simplecare(request):
    return HttpResponse('<h1><center>SimpleCare</center></h1>')
