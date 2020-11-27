import pandas as pd
"""
1. view로부터 입력데이터 획득
2. 해당 입력데이터와 일치하는 df 행의 드라마정보(1,2,3) 가져오기
3. 이 값들에 가중치를 부여해 리스트에 누적
4. 가장 큰 값 
"""

df = pd.read_csv('./formdata.csv') #폴더경로는 ./폴더명/파일명

# Drop cols (will not be used)
del df['date']
del df['age']
del df['gender']

# Column name list
col_names = list(df)
print(col_names)


# get user answer from view
def get_from_view(col):
    #test value
    val = ['내향형', '아니오', '학생', '학업과 자기계발, 음악과 노래, 정치, 건강과 위생',
           '예', '아니오', '국내 수도권', 1, 4, '아니오', '이과', '넉넉함', '예', '예',
           '예', '일상(하위 코미디)', '지상파', '18-6시', 'TV 또는 빔 프로젝터', '본방송']
    dic = {}
    for i, col in enumerate(col_names):
        dic[col] = val[i]
    return dic[col]


# input data
user_input_data = {}



placing_drama_values = {}

for col in range(col_names):
    user_input_data[col] = get_from_view(col)
    str_col_name = col
    search_value = user_input_data[col]
    tmp_list = df[str_col_name] == search_value
    tmp2_list = df[tmp_list]
    list





# Pick values of one column
# data filtering https://hogni.tistory.com/9
str_col_name = 'family'
search_value = 4
tmp_list = df[str_col_name] == search_value
tmp2_list = df[tmp_list]
print(list(tmp2_list['first']))









