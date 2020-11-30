import operator
from random import randrange
import pandas as pd
import csv
import sqlite3
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups')


weight_list = {}  # weight list

def process_weight(drama_code, step1, step2, step3):
    weight = 2  # 가중치
    for step in [step1, step2, step3]:
        step = list(filter(lambda e: e != '', step))  # 공백 값 제거
        for elem in step:
            elem = elem.replace(' ', '')  # 글자의 공백제거
            if elem in list(drama_code):
                weight_list[drama_code[drama_code == elem].index[0]] += weight
        weight /= 2


def solution(input_data):

    # Read formdata.csv
    form_df = pd.read_csv('./dramarama/static/data/formdata.csv')
    form_df.drop(['date'], axis='columns', inplace=True)
    form_df = form_df.fillna('')  # NaN값 제거

    # Column name list
    col_names = list(form_df)

    # Read dramadata.csv
    drama_df = pd.read_csv('./dramarama/static/data/dramadata.csv')
    data = list(drama_df['value'])
    # drama code
    drama_code = pd.Series(data, index=list(drama_df['id'].astype(str)))

    # DB Connection
    conn= sqlite3.connect('./drama_datas.sqlite3')



    for idx in list(drama_code.index):  # Initialize weight list
        weight_list[idx] = 0

    weight_df = pd.DataFrame()  # temp repository

    for col in col_names:  # turn all cols in input data
        if col in input_data.keys():  # check there's it
            if type(input_data[col]) == int:
                match = form_df[col] == input_data[col]
                weight_df = form_df[match]
            else:
                for ele in input_data[col]:  # turn all cols in list
                    match = (form_df[col].astype(str)).str.contains(ele)
                    weight_df = pd.concat([weight_df, form_df[match]])

            first = list(weight_df['first'])
            second = list(weight_df['second'])
            third = list(weight_df['third'])
            if not first: continue
            if not second: continue
            if not third: continue
            process_weight(drama_code, first, second, third)  # compute weight
            weight_df = pd.DataFrame()  # Initialize

    sorted_weight = sorted(weight_list.items(), key=operator.itemgetter(1), reverse=True)  # form: tuples in list
    drama_obj = drama_df[drama_df['id'].astype(str) == sorted_weight[randrange(3)][0]]

    return dict(drama_obj.iloc[0])