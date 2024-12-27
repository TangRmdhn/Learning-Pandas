import pandas as pd

df = pd.read_csv('data_mentah.csv')

print(df)

mising = df.columns[df.isnull().any()]

# df['Usia'].fillna(value=df['Usia'].mean(),inplace=True)

# df['Pendapatan'].fillna(value=df['Pendapatan'].median(),inplace=True)

df['Nama'].fillna(value='Tidak Diketahui',inplace=True)

duplicate = df[df.duplicated()]

print(duplicate)