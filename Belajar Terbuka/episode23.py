# Episode 23 - Latihan Percabangan - Kalkulator sederhana
# kalkulator sederhana
# 4 (angka1) + (operator) 5 (angka2) = 9(hasil)


# YANG DIBUTUHKAN
# 1. data user = angka_1, angka_2, operator (+,-,x,/)
# 2. cabangnya
# 3. hasil dan tampilannya (ELIF)

#codingan kalkulator sederhana
a=float(input("angka pertama\t= "))
op= input("operator(+,-,x,/)\t= ")
b=float(input("angka kedua\t= "))

#masuk ke percabangan
if op =="+":
        hasil = a+b
        print (f"hasilnya= {hasil}")
elif op =="-":
        hasil = a-b
        print (f"hasilnya= {hasil}")
elif op == "x" or op == "*" : #menambah jumlah dr aksi dengan reaksi yang sama
        hasil = a*b
        print (f"hasilnya= {hasil}")
elif op == "/":
        hasil = a/b
        print (f"hasilnya= {hasil}")
else:
        print("Hasil tidak terdeteksi, coba lagi")

print(10*"=", "AKHIR DARI PROGRAM", 10*"=")

