# Episode 31 - Operasi pada List
data_angka = [0,2,6,4,4,7,8,4,4,7,9,10,4,6,0,1,2,3,7,4,0,4,0,4,1,2,3,7]
print(f"data angka= {data_angka}")

# Count Data
    # bisa menghitung muncul berapa kali dalam data
    # biasanya dipakai untuk mendeteksi statistik

jumlah_angka4 = data_angka.count(4)
jumlah_angka0 = data_angka.count(0)
print(f" jumlah angka 4 dalam data angka= {jumlah_angka4}")
print(f" jumlah angka 0 dalam data angka= {jumlah_angka0}")

# Mengambil posisi data
data= ["aku","kamu", "dia"]
print(f"data= {data}")
 
index= data.index("kamu")
print(f"index dari data 'kamu'= {index}")

index1=data.index("aku")
print(f"index dari data 'aku'= {index1}")

# Mengurutkan List
print(f"data angka yang belum diurutkan= {data_angka}")
data_angka.sort()
print(f"data angka yang sudah diurutkan= {data_angka}")
data.sort()
print(f"data sring yang sudah diurutkan= {data}")
#Jika angka, maka dimulai dari terkecil ke terbesar, jika alfabet, maka dimulai dari A ke Z

# Membalik list
data_angka.reverse()
data.reverse()
print(f"data yang sudah disort lalu di reverse= \n{data_angka}\n{data}")