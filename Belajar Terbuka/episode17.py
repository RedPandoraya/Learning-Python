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
# Hasilnya akan False, karena Don't Die bukanlah penulisan judul yang benar karena ada tanda ('), sehingga tidak dihitung sebagai judul
