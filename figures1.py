import pandas as pd
import plotly.express as px
from math import isnan

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

####Convert Worksheet into csv

df = pd.read_csv('data/numerical_data.csv')
df['日期'] = pd.to_datetime(df['日期'], format='%d-%m-%Y')

##This figure shows the number of confirmed cases by date
df1 = pd.melt(df, id_vars=['日期'], value_vars=['確診人數', '死亡個案'], var_name='種類', value_name='人數')
fig1 = px.line(df1, x = '日期', y = '人數', color= '種類' , template="plotly_dark")
fig1.update_xaxes(title_text='日期')
fig1.update_yaxes(title_text='人數')

###This figure shows the other three statistics
df2 = pd.melt(df, id_vars=['日期'], value_vars=['醫管局當天呈報個案', '正住院接受檢查', '正受隔離'], var_name='種類', value_name='人數')
fig2 = px.line(df2, x = '日期', y = '人數', color= '種類' ,title='其他統計', template="plotly_dark")
fig2.update_xaxes(title_text='日期')
fig2.update_yaxes(title_text='人數')

##A string on the internet based on the latest figure
#make sure the data is available, if the data is not available, exclude by the loop
for i in reversed(range(len(df['確診人數']))):
    if isnan(df['確診人數'][i]) == False:
        confirmed_string = "最新確診人數:" + str(int(df['確診人數'][i]))
        break

for i in reversed(range(len(df['正受隔離']))):
    if isnan(df['正受隔離'][i]) == False:
        isolated_string = "最新隔離人數:" + str(int(df['正受隔離'][i]))
        break

for i in reversed(range(len(df['正住院接受檢查']))):
    if isnan(df['正住院接受檢查'][i]) == False:
        checking_string = "正接受撿查人數:" + str(int(df['正住院接受檢查'][i]))
        break

for i in reversed(range(len(df['死亡個案']))):
    if isnan(df['死亡個案'][i]) == False:
        death_string = "最新死亡人數:" + str(int(df['死亡個案'][i]))
        break
