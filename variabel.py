angka= "5" #ini adalah variabel/memory
berkoma= "12.5"
nama= "panda"
print(angka) #ini adalah outputnya
print(berkoma)
print("nama saya adalah", nama)

#type casting / ganti tipe data
#dapat dilakukan dengan function str() int() bool()
angka_int = 5
angka_str = str(angka_int)
angka_float = float(angka_str)
print("\n")
print(type(angka_int))
print(type(angka_str))
print(type(angka_float))

#meninput data
nama = input("nama saya adalah")
print ("Selamat Pagi", nama, ",Semoga harimu menyenangkan!")