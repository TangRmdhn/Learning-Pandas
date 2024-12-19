import pandas as pd

df = pd.read_csv('data_individu_kompleks.csv')

print(df)

'''
Kelompokkan data berdasarkan wilayah:
1. Hitung rata-rata pendapatan dan skor kepuasan di setiap wilayah.
2. Temukan wilayah dengan rata-rata skor kepuasan tertinggi.
'''
pendapatanSkor = df.groupby('Wilayah')[['Pendapatan','Skor Kepuasan']].mean().idxmax()

skorTertinggi = df.groupby('Wilayah')['Skor Kepuasan'].mean().idxmax()

'''
Analisis loyalitas:
1. Berapa persentase individu yang loyal di setiap kelompok usia?
2. Apakah ada hubungan antara tingkat pendidikan dan status loyalitas?
'''

kelompok = df.loc[df['Status Loyalitas'] == 'Loyal', ['Kelompok Usia','Status Loyalitas']].groupby('Kelompok Usia')['Status Loyalitas'].count()
# print(kelompok)


'''
Segmentasi berdasarkan pendapatan:
1. Buat kategori pendapatan menjadi: "Rendah" (< 5.000), "Menengah" (5.000-10.000), dan "Tinggi" (> 10.000).
2. Hitung jumlah individu dalam setiap kategori untuk setiap wilayah.
'''

'''
Individu dengan skor kepuasan rendah:
1. Cari individu dengan skor kepuasan di bawah rata-rata nasional.
2. Tampilkan data mereka dengan fokus pada wilayah, kelompok usia, dan tingkat pendidikan.
'''
'''
Eksplorasi data tambahan:
1. Tampilkan individu yang memiliki catatan tambahan.
2. Berapa rata-rata skor kepuasan mereka dibandingkan individu tanpa catatan?
'''

'''
Visualisasi pivot sederhana:
1. Gunakan pivot table untuk menampilkan rata-rata pendapatan berdasarkan wilayah dan tingkat pendidikan.
'''