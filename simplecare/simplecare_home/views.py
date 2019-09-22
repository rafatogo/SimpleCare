from django.shortcuts import render
from django.http import HttpResponse

def simplecare(request):
    return render(request, 'simplecare_home/simplecare_input_text.html')
