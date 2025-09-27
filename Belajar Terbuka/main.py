# Learning-Python

#episode 4 Mengenal Variabel
x=2
print("nilai x adalah= ", x)
y=3
print("nilai y adalah= ", y)
z=y-x
print("nilai y-x adalah= ", z)

#episode 5 Tipe Data
#1 angka = integer
a= 10
#2 angka dengan koma = float
a=5.5
#3 teks = string
a="belajar python"
#4 biner = boolean
a=True
a=False
#5 data kompleks
a=2+3j
print(a)

#episode 6 casting tipe data
#casting= mengubah tipe data
angka=10
castingangka=float(angka)
print(castingangka, type(castingangka))

#sama dengan casting ke tipe lainnya tapi sedikir berbeda untuk boolean
teks="" 
#jika teksnya diisi maka akan True, jika tika maka False
castingteks=bool(teks)
print(castingteks, type(castingteks))

angka=0
#selain angka 0, maka hasilnya akan True
castingangka=bool(angka)
print(castingangka, type(castingangka))

#episode 7 mengambil imput data dari user
data=input("masukkan data= ")
print("data yang dimasukkan adalah= ", data, type(data))

#mengubah tipe data inputan
data=int(input("masukkan angka= "))
print("angka yang dimasukkan adalah= ", data, type(data))
#sama halnya dengan tipe data float

data=bool(input("masukkan data= "))
print("data yang dimasukkan adalah= ", data, type(data))
#selain angka 0, maka hasilnya akan True

#ini branch baru