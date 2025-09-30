
# mengimpor library yang dibutuhkan
import numpy as np 
import pandas as pd

# memuat data dan inspeksi data
#df_kar = pd.read_csv("Employee_Data.csv")
df_kar = pd.read_csv("Coding Studio/Employee_Data.csv") #tergantung dimana diletakkannya filenya
print(df_kar)

# menampilkan 5 baris pertama data (inspeksi data)
print("\n5 BARIS PERTAMA DARI EMPLOYEE DATA= \n", df_kar.head())

# menampilkan informasi data
print("\nMENAMPILKAN INFORMASI DATA= \n", df_kar.info())

# melihat data yang hilang (missing data) dalam bentuk kolom
print("\nDATA YANG HILANG=\n ", df_kar.isnull().sum())
#hasilnya adalah ada data yang hilang pada kolom usia dan pengalaman (tahun)

# cleaning data
# kolom Usia akan diisi dengan AVERAGE 
# kolom Pengalaman (Tahun) akan diisi dengan MEDIAN

# USIA
average = df_kar ['Usia'].mean()
df_kar['Usia'].fillna(average, inplace = True) # perintah ini adalah untuk menimpa data yang kosong (opsional)
print("\nRATA-RATA USIA DARI DATA YANG ADA= \n"f'{average:.2f}') # menampilkan hasil rata-rata dengan 2 angka di belakang koma   

# PENGALAMAN (TAHUN)
median = df_kar['Pengalaman (Tahun)'].median()
df_kar['Pengalaman (Tahun)'].fillna(median, inplace = True)
print("\nNILAI TENGAH DARI PENGALAMAN KERJA DARI DATA KARYAWAN= \n", median) 

# agresi data atau grouping data
# mencari rata-rata kinerja berdasarkan departemen
rata_rata_kinerja = df_kar.groupby('Departemen')['Rating Kinerja'].mean()
print("\nRATA-RATA KINERJA PER DEPARTEMEN= \n",rata_rata_kinerja)

# mencari total usia dan pengalaman seluruh departemen
total_usia_pengalaman = df_kar.groupby('Departemen')[['Usia' , 'Pengalaman (Tahun)']].sum()
print("\nTOTAL JUMLAH USIA DAN PENGALAMAN KARYAWAN PER DEPARTEMEN= \n", total_usia_pengalaman)

# mencari jumlah karyawan per departemen
sum= df_kar ['Departemen'].value_counts()
print("JUMLAH KARYAWAN SETIAP DEPARTEMEN= \n", sum)

#filter data karyawan untuk menemukan karyawan dengan kinerja tertentu (dengan rating kinerja)
kinerja_tinggi= df_kar[df_kar['Rating Kinerja'] > 4.0] # Menentukan bahwa karyawan dengan kinerja tinggi adalah lebih dari 4
print("\nKARYAWAN DENGAN KINERJA TINGGI (LEBIH DARI 4)= \n", kinerja_tinggi)

#melihat karyawan departemen sales yang pengalamannya lebih dari 5 tahun
experience= df_kar[(df_kar['Departemen'] == 'Sales') & (df_kar['Pengalaman (Tahun)'] > 5)]
print("\nKARYAWAN YANG PENGALAMAN LEBIH DARI 5 TAHUN DI DEPARTEMEN SALES= \n", experience)

#membuat kolom baru dari data yang sudah ada
# KOLOM "Status Kinerja"
# Jika rating >= 4.5 dikategorikan "sangat baik", selain itu maka "baik"
df_kar['Status Kinerja'] = np.where(df_kar['Rating Kinerja'] >= 4.5, 'Sangat baik', "Baik")
print("\nKINERJA SEMUA KARYAWAN= \n", df_kar)
