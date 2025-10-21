# Episode 30 - Manipulasi list

data = ["aku", "kamu", "dia", "mereka"]
#index  0(-1)   1(-2)   2(-3)    3(-4)

# Mengambil data dari list
data0 = data [0]
print(f"indeks 0 dari data adalah= {data0}")

data_terakhir = data [-1]
print(f"indeks terakhir dari data adalah= {data_terakhir}")

data_slice = data [1:3] #mengambil data dari indeks 1 sampai sebelum 3
print(f"data slice dari indeks 1 sampai sebelum 3 adalah= {data_slice}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data dari list= {panjang_data}")


# MEMANIPULASI DATA DARI LIST
# 1. Menambahkan data pada list sesuai posisi
print(f"data sebelum ditambah= {data}")
data.insert(1,"kalian") #menambahkan data "kalian" pada indeks 1
print(f"data setelah ditambah= {data}")

# 2. Menambahkan data di akhir list
data.append ("kita") #menambahkan data "kita" di akhir list
print(f"menambahkan data 'kita' di posisi terakhir= {data}")

# 3. Menambahkan list dengan list
new= ["i","you","he","they"]
data.extend(new) #menambahkan list new ke list data
print(f"gabungan dari kedua data (list)= {data}")

# 4. Merubah data
# merubah data indeks 2 menjadi we are
data[2] = "we are"
print(f"perubahan pada data indeks 2= {data}")

# 5. Meremove data
data.remove ("we are") #penggunaan huruf kapital/tanda baca harus sesuai
print(f"data yang sudah diremore bagian 'we are'= {data}")

# 6. Meremove data paling akhir
data_akhir= data.pop()
print(f"data akhir yang telah di remove= {data}")
print(f"data terakhir= {data_akhir}")
