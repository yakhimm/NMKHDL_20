import pandas as pd
import numpy as np
from datetime import date
from gets import get_weather_air
import time

if __name__ == '__main__':
    #Tạo list chứa danh sách url
    lst = np.genfromtxt('../../data/models_url.csv', dtype = 'str')
    lst = lst[1:]

    df_list = []

    for i in range(len(lst)):
        try:
            dict_value = get_weather_air(lst[i])
            series_value = pd.Series(dict_value)
            df_list.append(series_value)
        except:
            i += 1
    df = pd.concat(df_list, axis = 1).T 
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    df.to_csv(f'../../data/models_data/{d}.csv', index = False)

    time.sleep(2)
    print('SCRAWL MODELS DATA SUCCESSFUL !!')
    time.sleep(2)