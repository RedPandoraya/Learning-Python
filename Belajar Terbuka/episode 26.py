# Episode 26 Continue dan Pass

# Continue dan Pass adalah perintah tambahan yang bisa digunakan pada perulangan (loop)
# Pass = berfungsi sebagai dummym dan tidak akan dieksekusi di terminal

a=10
while a<5:
    a+=1
    if a==3:
        pass #jadi ketika a=3 maka tidak akan dieksekusi
    print(a)

# Pass biasanya digunakan ketika ingin memunda atau belum tau aksi apa yang akan dilakukan, tapi ingin dibuat strukturnya dulu secara garis besar

# Continue = berfungsi untuk menghentikan/memodifikasi loop pada kondisi tertentu dan lanjut ke loop berikutnya
a=0
print(f"angka pada saat ini= {a}")

while a<5:
    a+=1
    print(f"angka saat ini setelah ditambah 1= {a}") #aksi 1

    if a==3:
        print("Hello world")
        continue  
        #jika tidak ada continue maka aksi 2 akan tetap dieksekusi
        #dengan continue maka ketika a=3 maka aksi 2 akan diganti menjadi hello world dan melanjutkan ke loop berikutnya
    print("apa kabar?") #aksi 2

print("selesai")
