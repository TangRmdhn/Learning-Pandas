import pandas as pd
import random
import numpy as np

# Membuat data kompleks yang lebih sulit untuk CSV
np.random.seed(42)

# Data untuk kolom
ids = range(1, 501)  # 500 data
names = [f"Individu-{i}" for i in ids]
genders = random.choices(["Laki-Laki", "Perempuan"], k=500)
age_groups = random.choices(["Remaja", "Dewasa", "Lansia"], k=500)
incomes = [round(random.uniform(2000, 20000), 2) for _ in ids]
education_levels = random.choices(["SMA", "Diploma", "Sarjana", "Magister", "Doktor"], k=500)
regions = random.choices(["Jawa", "Sumatera", "Kalimantan", "Sulawesi", "Papua"], k=500)
satisfaction_scores = [random.randint(1, 10) for _ in ids]
loyalty_status = random.choices(["Loyal", "Tidak Loyal"], k=500)
notes = [None if random.random() > 0.7 else f"Catatan-{i}" for i in ids]

# Membuat DataFrame
data = {
    "ID": ids,
    "Nama": names,
    "Jenis Kelamin": genders,
    "Kelompok Usia": age_groups,
    "Pendapatan": incomes,
    "Tingkat Pendidikan": education_levels,
    "Wilayah": regions,
    "Skor Kepuasan": satisfaction_scores,
    "Status Loyalitas": loyalty_status,
    "Catatan": notes
}

df = pd.DataFrame(data)

# Menyimpan data ke file CSV
df.to_csv("data_individu_kompleks.csv", index=False)

print("File 'data_individu_kompleks.csv' berhasil dibuat!")
