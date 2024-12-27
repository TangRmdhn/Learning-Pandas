import pandas as pd

# Data mentah
data = {
    "ID": [101, 102, 103, 104, 105, 106, 103, 107],
    "Nama": ["Ali", "Budi", "Citra", "Dina", "Eka", None, "Citra", "Gilang"],
    "Usia": [25, 30, None, 22, 19, 45, 22, 28],
    "Kota": ["Jakarta", "Bandung", "bandung", "Surabaya", "Jakarta", "Medan", "Bandung", "Surabaya"],
    "Pendapatan": [5000000, 7000000, None, 6000000, 4000000, 8000000, 6000000, None],
    "Tanggal_Bergabung": ["2022-01-15", "2021-07-12", "2021-07-12", "2023-03-10", None, "2020-09-05", "2021-07-12", "2022-11-25"],
    "Gender": ["Pria", "Pria", "Wanita", "Wanita", "Pria", None, "Wanita", "Pria"],
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menyimpan ke file CSV
df.to_csv("data_kompleks.csv", index=False)
print("File data_kompleks.csv telah dibuat.")
