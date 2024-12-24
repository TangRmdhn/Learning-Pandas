import pandas as pd
import random
import numpy as np

# Membuat data super kompleks untuk latihan pandas
np.random.seed(42)

# Parameter jumlah data
num_data = 2000

# Data untuk kolom
ids = range(1, num_data + 1)
names = [f"Individu-{i}" for i in ids]
genders = random.choices(["Laki-Laki", "Perempuan"], k=num_data)
ages = [random.randint(18, 65) for _ in ids]
education_levels = random.choices(["SMA", "Diploma", "Sarjana", "Magister", "Doktor"], k=num_data)
incomes = [round(random.uniform(1500, 30000), 2) for _ in ids]
spendings = [round(random.uniform(300, 20000), 2) for _ in ids]
working_hours = [random.randint(10, 80) for _ in ids]
regions = random.choices(["Urban", "Suburban", "Rural"], k=num_data)
promotions = random.choices(["Yes", "No"], k=num_data)
loyalty_score = [round(random.uniform(1, 100), 2) for _ in ids]
health_scores = [round(random.uniform(50, 100), 2) for _ in ids]
department = random.choices(["Finance", "Marketing", "HR", "IT", "Operations"], k=num_data)
experience_years = [random.randint(1, 40) for _ in ids]

# Kondisi hasil berdasarkan skor loyalitas dan kesehatan
outcomes = ["High Performer" if loyalty > 80 and health > 80 else "Average" if loyalty > 50 else "Low Performer" for loyalty, health in zip(loyalty_score, health_scores)]

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
    "Skor Kesehatan": health_scores,
    "Departemen": department,
    "Pengalaman (Tahun)": experience_years,
    "Hasil": outcomes
}

df = pd.DataFrame(data)

# Menyimpan data ke file CSV
df.to_csv("data_individu_super_kompleks.csv", index=False)

print("File 'data_individu_super_kompleks.csv' berhasil dibuat!")
