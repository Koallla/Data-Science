import pandas as pd

# url = 'https://drive.google.com/file/d/1JMYqXipZpz9Y5-vyxvLEO2Y1sRBxqu-U/view'
url = '2017_jun_final.csv'
def del_col_with_null(df_data):
    for col in df_data:
        if df_data[col].isnull().sum() and col != 'Язык.программирования':
            df.drop(col, axis=1, inplace=True)

        


df = pd.read_csv(url)
df.head()
df.shape
df.dtypes
df.isnull().sum()
del_col_with_null(df)
df = df.dropna()
df.shape
python_data = df[df['Язык.программирования'] == 'Python']
python_data.shape
grouped = python_data.groupby(by='Должность').head(207)
print(grouped)