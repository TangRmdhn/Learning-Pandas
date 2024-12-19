import pandas as pd

#Membaca Data csv
file_path = "data_penjualan.csv"
df = pd.read_csv(file_path)

#Menghapus row yang null
df.dropna()

#Menambah kolom yang menghitung total harga
df['Total'] = df['Jumlah'] * df['Harga']

#Menjumlahkan semua pendapatan
pendapatan = df['Total'].sum()
print(pendapatan)

#Mencari Produk yang terjual terbanyak
terbesar = df.loc[df.Jumlah.idxmax(),'Produk']

