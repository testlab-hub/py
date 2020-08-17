# PIVOT Table grouper
import pandas as pd

df = pd.read_csv("weather3.csv")
df['date'] = pd.to_datetime(df['date'])
print(df)
# print(type(df['date'][0]))
print('***********************************************')
example = df.pivot_table(index=pd.Grouper(key='date', freq='M'), columns='city')
print(example)
