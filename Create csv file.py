import pandas as pd
import random
import numpy as np

# Membuat data kompleks untuk mendekati kasus machine learning
np.random.seed(42)

# Data untuk kolom
ids = range(1, 1001)  # 1000 data
names = [f"Individu-{i}" for i in ids]
genders = random.choices(["Laki-Laki", "Perempuan"], k=1000)
ages = [random.randint(18, 60) for _ in ids]
education_levels = random.choices(["SMA", "Diploma", "Sarjana", "Magister", "Doktor"], k=1000)
incomes = [round(random.uniform(2000, 20000), 2) for _ in ids]
spendings = [round(random.uniform(500, 15000), 2) for _ in ids]
working_hours = [random.randint(20, 60) for _ in ids]
regions = random.choices(["Urban", "Suburban", "Rural"], k=1000)
promotions = random.choices(["Yes", "No"], k=1000)
loyalty_score = [round(random.uniform(1, 100), 2) for _ in ids]
outcomes = ["Success" if score > 70 else "Failure" for score in loyalty_score]

# Membuat DataFrame
data = {
    "ID": ids,
    "Nama": names,
    "Jenis Kelamin": genders,
    "Usia": ages,
    "Tingkat Pendidikan": education_levels,
    "Pendapatan": incomes,
    "Pengeluaran": spendings,
    "Jam Kerja": working_hours,
    "Wilayah": regions,
    "Promo": promotions,
    "Skor Loyalitas": loyalty_score,
    "Hasil": outcomes
}

df = pd.DataFrame(data)

# Menyimpan data ke file CSV
df.to_csv("data_machine_learning.csv", index=False)

print("File 'data_machine_learning.csv' berhasil dibuat!")
