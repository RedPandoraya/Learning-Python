#episode 17 Operasi dan Manupulasi String (pt2)

# Operator method ada banyak sebenarnya bisa digoogling dan dicari, kali ini cuma beberapa aja yang akan dibahas

# Merubah case dan string (Uppercase/Lowercase)
# Uppercase
a = "sup"
print('normal= ', a)
a = a.upper()
print('upper= ', a)

# Lowercase
a = "Q sanqat CantiQue"
print('normal= ', a)
a = a.lower()
print('lower= ', a)

# Pengecekan dengan isX Method
a= "masbro"
lower= a.islower() # Hasilnya akan dalam bentuk boolean
print('Apakah lower= ', str(lower))
upper= a.isupper() # Hasilnya akan dalam bentuk boolean
print('Apakah upper= ', str(upper))

# Kemudian masih ada macam macam method yang bisa di coba (dari YT Kelas Terbuka)
# 1. isaplha()   = untuk memeriksa apakah semuanya huruf
# 2. isalnum()   = untuk memeriksa apakah karakternya terdiri dari huruf dan angka
# 3. isdecimal() = untuk memeriksa apakah angka saja
# 4. isspace()   = untuk memeriksa spasi, tab, newline (\n)
# 5. istitle()   = untuk memeriksa apakah semua kata dimulai dari huruf kapital

# contoh dari istitle()
j='Do Not Die'
cek= j.istitle()
print('Apakah', j ,'Bisa disebut sebagai judul= ', str(cek))

j="Don't Die"
cek= j.istitle()
print('Apakah', j ,'Bisa disebut sebagai judul= ', str(cek))
#Hasilnya akan False, karena Don't Die bukanlah penulisan judul yang benar karena ada tanda ('), sehingga tidak dihitung sebagai judul

# Mengecek komponen startswith(), dan endswith()
start = "Annyeong haseyo".startswith('Annyeong')
print('dimulai dari Annyeong= ', str(start)) #True
end = "Annyeong haseyo".endswith('Haseyo')
print('diakhiri dengan Haseyo= ', str(end)) #hasilnya akan Falase karena "H dari "Haseyo" itu huruf kapital

# Tanda [] arinya list adalah untuk meletakkan kumpulan data
# Penggabungan komponen pengabungan/join(), dan pemisahan/split()

# JOIN
a ='aku','anak','sehat'
join = ' '.join(a) #dalam tanda kutip jika tidak diberi space maka kata-katanya akan menempel
print(join)

p= 'aku,anak,sehat,tubuhku,kuat'
print(p.split(','))

# Alokasi karakter rjust(),     ljust(),  center()
#                  rata kanan, rata kiri, tengah

r= "rata kanan".rjust(20) #rata kanan ada 10 kata, jika rata kanan maka bagian kiri masih ada 10 "space"
print(".",r,".")
l= "rata kiri".ljust(20)
print(".",l,".")
c= "tengah".center(20)
print(".",c,".")

# Kebalikannya disebut sebagai strip()
c= c.strip(" ") # isi tanda "" sesuai dengan apa yg kosong sebelumnya
print(".",c,".")

    # MISALNYA
c= "tengah".center(20,"'") # ada pemisah setiap kata dengan tanda single quote (') 
print(".",c,".")
c= c.strip("'") # isi tanda "" sesuai dengan apa yg kosong sebelumnya, yaitu ('), maka tanda (') akan hilang
print(".",c,".")
