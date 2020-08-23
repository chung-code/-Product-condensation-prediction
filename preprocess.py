#%%
import pandas as pd
import numpy as np
import math
import openpyxl 
from openpyxl import load_workbook
import operator

raw_binning = pd.read_excel(r'C:\Users\신충현\Desktop\yonsei\학부연구생\2020 날씨 빅데이터 콘테스트\python_preprocess\data preprocess(python)_0621.xlsm',sheet_name="real_data")

# plant1_train.tem_in_loc1_B	
# plant1_train.hum_in_loc1_B	
# plant1_train.tem_coil_loc1_B	
# plant1_train.tem_in_loc2_B	
# plant1_train.hum_in_loc2_B	
# plant1_train.tem_coil_loc2_B	
# plant1_train.tem_in_loc3_B	
# plant1_train.hum_in_loc3_B	
# plant1_train.tem_coil_loc3_B	
# plant1_train.tem_out_loc1_B	
# plant1_train.hum_out_loc1_B	
# plant1_train.cond_loc1_B	
# plant1_train.cond_loc2_B	
# plant1_train.cond_loc3_B	
# 기온(°C)_B	
# 델타기온_B	
# 습도(%)_B	
# 델타습도_B	
# 이슬점온도(°C)_B


feature = []
for i in range(len(raw_binning)):
    #raw_binning.iloc[i].loc['기온(°C)_B'] == nan

    raw_binning['델타기온_B'].fillna("X")
    
    feature_combined = str(raw_binning.iloc[i].loc['기온(°C)_B']) + str(raw_binning.iloc[i-1].loc['기온(°C)_B']) + str(raw_binning.iloc[i].loc['델타기온_B']) + str(raw_binning.iloc[i-1].loc['델타기온_B'])
    feature.append(feature_combined)

raw_binning['feature'] = feature

data = raw_binning.loc[:,['number','timeline','feature','plant1_train.tem_in_loc1_B']]

one_devide_list = []
for i in range(len(data)):
    one_devide = data.iloc[i].loc['feature']   
    find_one = data.loc[data['feature'] == one_devide, 'timeline'].values
    one_devide_list.append(find_one)

data['one_devide'] = one_devide_list
#%%
second_devide_list = []
for i in range(len(data)):
    second_devide = data.iloc[i-1].loc['feature']
    find_scond = data.loc[data['feature'] == second_devide,'timeline'].values
    
    index_number = []
    for k in find_scond:
        index_number.append(data.loc[data['timeline'] == k, 'number'].values)
    #addition = []
    #for q in range(len(index_number)):
         #addition.append(int(1))
    
    #indexing = list(map(operator.add, index_number, addition))
print(index_number)

#%%
    find_second_Fake = []
    for j in indexing:
        find_second_Fake.append(data.loc[data['number'] == j, 'timeline'].values)
    
    standard_timeline = data.iloc[i].loc['one_devide']
    find_second_Real = []
    for p in standard_timeline:
        if p in find_second_Fake:
            find_second_Real.append(p)
        else:
            continue
    
    second_devide_list.append(find_second_Real)

data['second_devide'] = second_devide_list        


print(data['one_devide','second_devide'])