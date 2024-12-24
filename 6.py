import pandas as pd

df = pd.read_csv('data_individu_super_kompleks.csv')

print(df)

'''
Statistik Deskriptif:
Hitung rata-rata, median, dan standar deviasi untuk kolom Pendapatan dan Pengeluaran.
Tampilkan jumlah individu di setiap tingkat pendidikan.
'''
rata = df[['Pendapatan','Pengeluaran']].mean()
med = df[['Pendapatan','Pengeluaran']].median()
std = df[['Pendapatan','Pengeluaran']].std()

banyakPendidik = df['Tingkat Pendidikan'].value_counts()
'''
Analisis Demografis:
Berapa jumlah individu berdasarkan wilayah (Wilayah) dan jenis kelamin (Jenis Kelamin)?
Tampilkan persentase individu berusia di atas 40 tahun di setiap departemen.
'''
wilayahkelamin = df.groupby(['Wilayah','Jenis Kelamin'])['Nama'].count()

percen = (df.loc[df['Usia'] >= 40]['Nama'].count()/df['Nama'].count())*100
print(f"{percen}%")
'''
Analisis Kinerja:
Berapa rata-rata Skor Loyalitas dan Skor Kesehatan untuk setiap hasil (Hasil)?
Temukan departemen dengan proporsi tertinggi dari individu dengan hasil High Performer.
'''


'''
Promosi dan Loyalitas:
Apakah individu yang menerima promosi (Promo = Yes) memiliki rata-rata Skor Loyalitas lebih tinggi dibandingkan yang tidak?
Hitung persentase individu dengan hasil High Performer di antara mereka yang menerima promosi.
'''


'''
Segmentasi Usia:
Bagi data ke dalam kelompok usia berikut: 18–30, 31–45, 46–60, dan 61+.
Hitung rata-rata Pendapatan dan Pengeluaran untuk setiap kelompok usia.
'''

'''
Korelasi:
Apakah terdapat korelasi antara Jam Kerja dan Pendapatan?
Apakah Skor Loyalitas berbanding lurus dengan Pengeluaran?
'''

'''
Eksplorasi Tambahan:
Temukan individu dengan Skor Kesehatan di bawah rata-rata nasional dan Pengalaman (Tahun) di atas 30 tahun.
Tampilkan 10 individu dengan rasio Pendapatan terhadap Pengeluaran tertinggi.
'''