import pandas as pd
import numpy as np
from datetime import date
from gets import get_weather_air

#Tạo list chứa danh sách url
lst = np.genfromtxt('./data/url.csv', dtype = 'str')
lst = lst[1:]

df_list = []

for i in lst:
    dict_value = get_weather_air(i)
    series_value = pd.Series(dict_value)
    df_list.append(series_value)
    
df = pd.concat(df_list, axis = 1).T 

today = date.today()
d = today.strftime("%b-%d-%Y")
df.to_csv(f'./data/data/{d}.csv', index = False)