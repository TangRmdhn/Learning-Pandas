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
# Bagaimana cara mencari persentase?

puas = df.loc[df['Status Loyalitas'] == 'Loyal', ['Tingkat Pendidikan','Status Loyalitas']].groupby('Tingkat Pendidikan')['Status Loyalitas'].count()

'''
Segmentasi berdasarkan pendapatan:
1. Buat kategori pendapatan menjadi: "Rendah" (< 5.000), "Menengah" (5.000-10.000), dan "Tinggi" (> 10.000).
2. Hitung jumlah individu dalam setiap kategori untuk setiap wilayah.
'''
def kategori(gaji):
    if gaji < 5000:
        return 'Rendah'
    elif gaji >= 5000 and gaji <= 10000:
        return 'Menengah'
    else:
        return 'Tinggi'

df['Kategori'] = df['Pendapatan'].apply(kategori)
print(df)

wilayah = df.groupby(['Kategori','Wilayah'])['Nama'].count()

'''
Individu dengan skor kepuasan rendah:
1. Cari individu dengan skor kepuasan di bawah rata-rata nasional.
2. Tampilkan data mereka dengan fokus pada wilayah, kelompok usia, dan tingkat pendidikan.
'''
bawahrata = df.loc[df['Skor Kepuasan'] < df['Skor Kepuasan'].mean()]

bawahratakel = bawahrata.groupby(['Wilayah','Kelompok Usia','Tingkat Pendidikan'])['Nama'].count()

'''
Eksplorasi data tambahan:
1. Tampilkan individu yang memiliki catatan tambahan.
2. Berapa rata-rata skor kepuasan mereka dibandingkan individu tanpa catatan?
'''

catat = df[df['Catatan'].notnull()]

ratacatat = df[df['Catatan'].notnull()]['Skor Kepuasan'].mean()
ratatanpacatat = df[df['Catatan'].isnull()]['Skor Kepuasan'].mean()


'''
Visualisasi pivot sederhana:
1. Gunakan pivot table untuk menampilkan rata-rata pendapatan berdasarkan wilayah dan tingkat pendidikan.
'''

ratadapat = df.groupby(['Wilayah','Tingkat Pendidikan'])['Pendapatan'].mean()