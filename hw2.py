import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



url = 'https://uk.m.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8#%D0%9D%D0%B0%D1%80%D0%BE%D0%B4%D0%B6%D1%83%D0%B2%D0%B0%D0%BD%D1%96%D1%81%D1%82%D1%8C'
match = 'Коефіцієнт народжуваності в регіонах України'

# def writer(data):
#     with open('data.json', 'w', encoding='utf-8') as file:
#         data.to_json(file, orient="columns")


# try:
#     df = pd.read_json('data.json', orient='values')
# except ValueError:
#     df = pd.read_html(url, match=match)[0]
#     writer(df)
#     df = pd.read_json('data.json', orient='values')



df = pd.read_html(url, match=match, thousands='.', decimal=',')[0]

head_data = df.head()
print(head_data)
shape = df.shape
df.replace("—", np.nan, inplace=True)
dtypes = df.dtypes
df = df.astype({'2014': np.float64, '2019': np.float64})
col_isnull_sum = df.isnull().sum()
df.drop([27], inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)
df[df['2019'] > df['2019'].mean()]['Регіон']
max_val_2014 = df.loc[df['2014'] == df['2014'].max()]['Регіон']
df[['Регіон', '2019']].plot.bar(rot=0)
plt.show()
