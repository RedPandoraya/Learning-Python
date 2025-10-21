#Episode 28 - Latihan Perulangan

#Looping segtigia bintang
#*
#**
#***
#****
#*****

# ini adalah contoh yang manual

#segitiga yang akan dibuat = 
sisi = 4
    #1. dengan menggunakan for
count=1
for i in range (sisi):
    print ("*"*count)
    count+=1

    #2. dengan menggunakan while
count = 1
while True:
    print ("*"*count)
    count+=1

    if count > sisi:
        break

    #3. hanya menggunakan angka ganjil 
count = 1
while True:
    if (count%2):
        print("*"*count)
        count +=1
    else:
        count +=1 
        continue
    if count > sisi:
        break

    #4. Segitiga sama kaki dan ganjil
count = 1
spasi = 5
while True:
    if (count%2):
        print(" "*spasi, "+"*count)
        spasi -=1
        count +=1
    else:
        count +=1
        continue
    if count > sisi:
        break