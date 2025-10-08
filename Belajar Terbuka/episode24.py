# Episode 24 - For Loop (Perulangan)

# Perulangan (loop)
a=1
print(a)
a=a+1
print(a)
a=a+1
print(a)
a=a+1
print(a)
#ini tidak efektif jika ingin ditambah terus

#for kondisi:
    #aksi

#for i in range (5)
# = untuk semua angka di range (5) akan diberi i

a2=[0,1,2,3,4] # ini adalah bentuk dari list
print(a2)

for i in a2:
        print(f"i sekarang= {i}")

a3=range(5) #range akan dimulai dari angka 0 jadi (0-4)
for i in a3:
        print(f"i sekarang= {i}")

a3= range(1,5) #range akan dimulai dari angka 1, dan diakhiri dengan angka 4 (5 tidak dihitung)
for i in a3:
        print(f"i sekarang= {i}")
        
#Note : tujuan for adalah untuk terus mengulang apa yang ada di bawha perintah FOR atau bisa disebut looping

str= "halo, salam kenal"

for a in str: #a disini adalah sebagai variabel sehingga bebas sebenarnya mau pakai apa aja
        print(a)
        