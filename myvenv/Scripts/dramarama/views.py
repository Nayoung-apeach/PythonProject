from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    return render(request, 'dramarama/index.html')

def go_form(request):
    return render(request, 'dramarama/who-you-are.html')