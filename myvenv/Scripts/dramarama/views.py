from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from dramarama import main_solution

def index(request):
    return render(request, 'dramarama/index.html')

@method_decorator(csrf_exempt)
def form(request):
    return render(request, 'dramarama/form.html')

@method_decorator(csrf_exempt)
def result(request):
    input_form = request.POST

    result = {'test':main_solution.solution(input_form)} # input_form['age']
    return render(request, 'dramarama/result.html', result)
