import pandas as pd

df = pd.read_csv("data_mahasiswa.csv")

#menghapus baris yang terdapat null
dfhapus = df.dropna()

#menghapus nim yang duplikat
dfdup = dfhapus.drop_duplicates('NIM')

#Rata-rata jumlah nim
mean = dfdup['NIM'].mean()

jumlah = dfdup.groupby('Jurusan')['Nama'].count()
print(jumlah)

#Nama Mahasiswa IPK Tertinggi
tertinggi = dfdup.loc[dfdup['IPK'].idxmax(), 'Nama']