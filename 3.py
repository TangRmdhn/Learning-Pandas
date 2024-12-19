import pandas as pd

df = pd.read_csv('data_mahasiswa_kompleks.csv')

print(df)

# Tampilkan jumlah mahasiswa aktif dan tidak aktif.
mAktif = df.groupby('Aktif')['Nama'].count()

# Hitung rata-rata IPK berdasarkan jurusan.
rataJur = df.groupby('Jurusan')['IPK'].mean()

# Cari mahasiswa dengan skor tes tertinggi dan tampilkan nama, jurusan, dan skor tesnya.
tertinggi = df.loc[df['Skor Tes'].idxmax(), ['Nama','Jurusan','Skor Tes']]

# Tampilkan 5 mahasiswa dengan usia tertua.
tertua = df.sort_values(by=['Usia']).tail(5)

# Hitung jumlah mahasiswa per tahun angkatan.
JumlahM = df.groupby('Angkatan')['Nama'].count()
# print(JumlahM)

# Tampilkan mahasiswa dengan catatan tambahan (kolom Catatan tidak kosong).
catatan = df[df['Catatan'].notnull()]
print(catatan)

# Cari jurusan yang memiliki rata-rata IPK tertinggi.
Rating = df.groupby('Jurusan')['IPK'].mean().idxmax()

# Tambahkan kolom baru bernama Lulus yang berisi "Ya" jika IPK >= 3.0 dan "Tidak" jika kurang.

def categorize(lulus):
    if lulus >= 3:
        return 'Ya'
    elif lulus < 3:
        return 'Tidak'
    
df['Lulus'] =  df['IPK'].apply(categorize)

# print(df)