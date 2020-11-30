from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import os
import pandas as pd

from dramarama import main_solution as sol

def index(request):
    return render(request, 'dramarama/index.html')

@method_decorator(csrf_exempt)
def form(request):
    return render(request, 'dramarama/form.html')

@method_decorator(csrf_exempt)
def result(request):
    input_form = request.POST
    """
    FORMDATA_DIR = os.path.join(os.path.relpath(), '/datas_csv/formdata.csv')
    with open(FORMDATA_DIR, encoding='utf-8') as form_csv:
        reader = csv.DictReader(form_csv, delimiter=',')
        form_df = pd.DataFrame(reader)

    DRAMADATA_DIR = os.path.join(os.path.relpath(), '/datas_csv/dramadata.csv')
    with open(DRAMADATA_DIR, encoding='utf-8') as drama_csv:
        reader = csv.DictReader(drama_csv, delimiter=',')
        drama_df = pd.DataFrame(reader)
    """

    result = {'test':sol.solution(dict(input_form))}

    return render(request, 'dramarama/result.html', result)
