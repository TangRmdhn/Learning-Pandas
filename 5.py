import pandas as pd

df = pd.read_csv('data_machine_learning.csv')

print(df.head())

'''
Statistik Deskriptif:
Hitung rata-rata, median, dan standar deviasi untuk pendapatan dan pengeluaran.
Temukan jumlah individu di setiap kategori tingkat pendidikan.
'''
rata = df[['Pengeluaran','Pendapatan']].mean()
median = df[['Pengeluaran','Pendapatan']].median()
std = df[['Pengeluaran','Pendapatan']].std()

pendidik = df['Tingkat Pendidikan'].value_counts()
'''
Kelompokkan Data:
Berapa rata-rata pengeluaran dan jam kerja berdasarkan wilayah?
Tampilkan jumlah individu dengan hasil "Success" dan "Failure" di setiap kelompok usia (18-30, 31-45, 46-60).
'''
keluarjam = df.groupby('Wilayah')[['Pengeluaran','Jam Kerja']].mean()

# Sukses = df['Hasil'].value_counts()
def usia(umur):
    if umur >= 18 and umur <= 30:
        return '18-30'
    elif umur >= 31 and umur <= 45:
        return '31-45'
    elif umur >= 46 and umur <= 60:
        return '46-60'
df['Kelompok Usia'] = df['Usia'].apply(usia)
hasil_per_kelompok = df.groupby(['Kelompok Usia', 'Hasil'])['Nama'].count()
'''
Analisis Promosi:
Apakah individu yang menerima promosi memiliki skor loyalitas rata-rata lebih tinggi dibandingkan yang tidak?
Hitung persentase individu dengan hasil "Success" di antara mereka yang menerima promosi.
'''
promosi = df.groupby('Promo')['Skor Loyalitas'].mean()

promo_success_rate = (df[(df['Promo'] == 'Yes') & (df['Hasil'] == 'Success')].shape[0] / 
                      df[df['Promo'] == 'Yes'].shape[0]) * 100
# print(f"Persentase Success di antara yang menerima promosi: {promo_success_rate:.2f}%")
'''
Segmentasi Berdasarkan Pendapatan:
Buat kategori pendapatan menjadi: "Rendah" (< 5.000), "Menengah" (5.000-10.000), dan "Tinggi" (> 10.000).
Berapa rata-rata skor loyalitas untuk setiap kategori pendapatan?
'''
def dapat(gaji):
    if gaji < 5000:
        return 'Rendah'
    elif gaji >= 5000 and gaji <= 10000:
        return 'Menengah'
    else:
        return 'Tinggi'
df['Pendapatan'] = df['Pendapatan'].apply(dapat)

rataskor = df.groupby('Pendapatan')['Skor Loyalitas'].mean()
'''
Identifikasi Korelasi:
Apakah ada hubungan antara jam kerja dan skor loyalitas? (Gunakan pandas untuk perhitungan korelasi).
Temukan wilayah dengan rata-rata skor loyalitas tertinggi dan lowest.
'''
korelasi = df[['Jam Kerja', 'Skor Loyalitas']].corr()

wilayahrata = df.groupby('Wilayah')['Skor Loyalitas'].mean()

'''
Analisis Kinerja Berdasarkan Pendidikan:
Tampilkan distribusi hasil "Success" dan "Failure" di setiap tingkat pendidikan.
Berapa rata-rata pengeluaran untuk individu dengan hasil "Success" dibandingkan dengan "Failure"?
'''
hasilpendidik = df.pivot_table(
    index='Tingkat Pendidikan',
    columns='Hasil',
    values='Nama',
    aggfunc='count',
    fill_value=0
)

pengeluaran = df.groupby('Hasil')['Pengeluaran'].mean()

'''
Eksplorasi Data Tambahan:
Tampilkan individu dengan skor loyalitas tertinggi di setiap wilayah.
Cari individu dengan skor loyalitas di atas rata-rata nasional dan pendapatan di bawah rata-rata nasional. Apa karakteristik mereka?
'''
tinggiloyal = df.loc[df.groupby('Wilayah')['Skor Loyalitas'].idxmax(), ['Wilayah','Nama','Skor Loyalitas']]

skortertinggi = df.loc[df['Skor Loyalitas'].idxmax()]
skorterendah = df.loc[df['Skor Loyalitas'].idxmin()]