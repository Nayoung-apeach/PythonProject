from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os
import csv
import pandas as pd
from dramarama.models import Drama

from dramarama import main_solution as sol

def index(request):
    return render(request, 'dramarama/index.html')

@method_decorator(csrf_exempt)
def form(request):
    return render(request, 'dramarama/form.html')

@method_decorator(csrf_exempt)
def result(request):
    input_form = request.POST

    """ **[경고] 이 코드는 절대로 실행되선 안됩니다. 주석 풀지 마세요.
    DRAMADATA_DIR = 'dramarama/static/data/dramadata.csv'
    with open(DRAMADATA_DIR, newline='', encoding='utf-8') as drama_csv:
        reader = csv.DictReader(drama_csv)
        for row in reader:
            Drama.objects.create(
                id = row['id'],
                title = row['title'],
                channel = row['channel'],
                info_url = row['information']
            )
    DB insert """

    result = {'test':sol.solution(dict(input_form))}

    return render(request, 'dramarama/result.html', result)