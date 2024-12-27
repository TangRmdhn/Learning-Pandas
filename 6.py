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
# print(f"{percen}%")
'''
Analisis Kinerja:
Berapa rata-rata Skor Loyalitas dan Skor Kesehatan untuk setiap hasil (Hasil)?
Temukan departemen dengan proporsi tertinggi dari individu dengan hasil High Performer.
'''
rataloyal = df.groupby('Hasil')['Skor Loyalitas'].mean()
ratasehat = df.groupby('Hasil')['Skor Kesehatan'].mean()

#no 2 maksudnya?
'''
Promosi dan Loyalitas:
Apakah individu yang menerima promosi (Promo = Yes) memiliki rata-rata Skor Loyalitas lebih tinggi dibandingkan yang tidak?
Hitung persentase individu dengan hasil High Performer di antara mereka yang menerima promosi.
'''
promoyesno = df.groupby('Promo')['Skor Loyalitas'].mean()

promohigh = df.loc[df['Hasil'] == 'High Performer']
promohighyes = promohigh.loc[promohigh['Promo'] == 'Yes']
percenyeshigh = (promohighyes['Nama'].count()/promohigh['Nama'].count())*100
# print(f"{percenyeshigh.round(2)}%")
'''
Segmentasi Usia:
Bagi data ke dalam kelompok usia berikut: 18-30, 31-45, 46-60, dan 61+.
Hitung rata-rata Pendapatan dan Pengeluaran untuk setiap kelompok usia.
'''
def kelompok(umur):
    if umur >= 18 and umur <= 30:
        return "18-30"
    elif umur >= 31 and umur <= 45:
        return "31-45"
    else:
        return "61+"
df['Kelompok Usia'] = df['Usia'].apply(kelompok)

pendapatan = df.groupby('Kelompok Usia')['Pendapatan'].mean()
Pengeluaran = df.groupby('Kelompok Usia')['Pengeluaran'].mean()
'''
Korelasi:
Apakah terdapat korelasi antara Jam Kerja dan Pendapatan?
Apakah Skor Loyalitas berbanding lurus dengan Pengeluaran?
'''
korelasi1 = df[['Jam Kerja', 'Pendapatan']].corr()

korelasi2 = df[['Skor Loyalitas', 'Pengeluaran']].corr()
'''
Eksplorasi Tambahan:
Temukan individu dengan Skor Kesehatan di bawah rata-rata nasional dan Pengalaman (Tahun) di atas 30 tahun.
Tampilkan 10 individu dengan rasio Pendapatan terhadap Pengeluaran tertinggi.
'''
skorsehatrata = df['Skor Kesehatan'].mean()
orang = df.loc[df['Skor Kesehatan'] < skorsehatrata].loc[df['Pengalaman (Tahun)'] > 30]


df['Rasio'] = df['Pendapatan']/df['Pengeluaran']

tertinggi = df.sort_values(by=['Rasio'],ascending=False).head(10)