# Episode 18 Format String

# 1. String
#n = "world"
#str ="hello",n
#print(str)
# ini lumayan ribet jika misalnya string dalam str masih mau ditambahin selain variable n
# MAKA :
n = "World"
format_str=f"Hello {n}"
print(format_str)

# 2. Boolean
b = True
format_bool= f"boolean = {b}"
print(format_bool)

# 3. Angka
a= 2005.6577
format_a= f"jumlah= {a}", type(a) #hasil formatnya bisa dicasting sesuai keinginan
print(format_a)

#-Angka (bilangan bulat)
a = 15
format_a = f"bilangan bulat= {a:d}" # :d adalah untuk menampilkan bahwa a adalah bilangan bulat
print(format_a)

#-Angka (Bilangan desimal)
a= 2005.6577
format_a = f"bilangan dengan 2 angka di belakang koma= {a:.2f}" # . = desimal, 2 = 2 angka, f = float
print (format_a)

#-Angka (Bilangan dengan ordo Ribuan)
a= 1000000
format_a=f"sejuta= {a:,}" #hasilnya akan otomatis diletakkan koma (,) setiap 3 angka
print(format_a)

#-Angka(Leading Zero)
a= 2005.6577
format_a= f"desimal leading zero= {a:010.3f}" 
#akan ada 10 ruang karakter (angka) yang akan ditampilkan termasuk koma, dan mengambil 3 angka dibelakang koma
print(format_a)

#-Angka (tanda "+", dan "-")
minus = -10
plus = 10
format_m= f"minus= {minus:+d}" # diberi tanda "+" agar nanti kelihatan yang mana plus
format_p= f"plus= {plus:+d}" \
#bisa juga digabung dengan desimal :
#format_p=f"plus= {plus:+.2f}"
print("tanda minus= ", format_m)
print("tanda plus= ", format_p)


#-Angka (Memformat Persen (%))
persen= 0.025
format_p= f"1/4 dari 100 adalah= {persen:.2%}" #ini adalah format untuk menggabungkan persen dan desimal
print(format_p)

