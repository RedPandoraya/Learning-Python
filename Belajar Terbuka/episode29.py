#Episode 29 - List

# Kumpulan data number
data_angka= [1,2,3,4,5,6,7,8,9,0]

# Kumpulan data string
data_str = ["aku","kamu","dia","mereka"]

# Kumpulan data bool
data_bool = [True, False, True, True]

# Kumpulan data campuran
data_mix = [1, "aku", True, 3.14, False]


# CARA MEMBUAT LIST
data_range = range (0,10,2) #Artinya angka yang akan muncul nanti adalah 0 sampai 10(9) (10 tidak dihitung) dengan kelipatan 2
                            #Dibaca Start, Stop, Step
data_list = list (data_range)
print(data_list)

# Membuat list dengan for loop, list comprehension
list_for = [i for i in range (0,10)] #artinya i dimana i dalam range 0-9
print(f"Membuat list dengan loop= {list_for}")
#i dalam for bisa dipangkatin dengan cara **2
list_for_pangkat = [i**2 for i in range (0,10)] #artinya i dimana i dalam range 0-9
print(f"Membuat list dengan loop lalu dipangkat 2= {list_for_pangkat}")

# Membuat list menggunakan for pake if
for_if = [i for i in range (0,10) if i != 5] #artinya i dimana i dalam range 0-9 kecuali angka 5
print(f"membuat list dengan menggunakan forif= {for_if}")

# Membuat list dengan angka genap aja
for_if_genap= [i for i in range (0,10) if i%2 ==0] #artinya i dimana i dalam range 0-9 yang habis dibagi 2
print(f"list untuk angka genap= {for_if_genap}")

# Membuat list dengan angka ganjil aja
for_if_ganjil= [i for i in range (0,10) if i%2 !=0] #artinya i dimana i dalam range 0-9 yang tidak habis dibagi 2
print(f"list untuk angka ganjil= {for_if_ganjil}")