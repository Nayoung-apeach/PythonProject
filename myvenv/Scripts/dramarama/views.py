from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    context = {}
    template_name = 'dramarama/index.html'
    return render(request, template_name)

