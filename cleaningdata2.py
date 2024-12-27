import pandas as pd

# Membaca data dari file CSV
df = pd.read_csv('data_kompleks.csv')

# Mengecek missing values
print("Jumlah missing values per kolom sebelum pembersihan:")
print(df.isnull().sum())

# Mengisi missing values
df['Usia'] = df['Usia'].fillna(df['Usia'].mean().round())
df['Pendapatan'] = df['Pendapatan'].fillna(df['Pendapatan'].median())
df['Nama'] = df['Nama'].fillna('Tidak Diketahui')
df['Gender'] = df['Gender'].fillna('Tidak Diketahui')
df['Tanggal_Bergabung'] = df['Tanggal_Bergabung'].fillna('2022-01-01')

# Menghapus duplikasi
duplikat = df[df.duplicated(subset='ID')]
print("\nData duplikat berdasarkan ID:")
print(duplikat)
df = df.drop_duplicates(subset='ID')

# Encoding kolom Gender
def encoding(gender):
    if gender == 'Pria':
        return 0
    elif gender == 'Wanita':
        return 1
    else:
        return 2

df['Gender_Encoded'] = df['Gender'].apply(encoding)

# Normalisasi kolom Pendapatan
df['Pendapatan_Normalisasi'] = (df['Pendapatan'] - df['Pendapatan'].min()) / (df['Pendapatan'].max() - df['Pendapatan'].min())

# Menggabungkan kolom Nama dan Kota menjadi Identitas
df['Identitas'] = df['Nama'] + " dari " + df['Kota']

# Mengecek hasil akhir
print("\nJumlah missing values per kolom setelah pembersihan:")
print(df.isnull().sum())
print("\nData hasil pembersihan:")
print(df.head())
