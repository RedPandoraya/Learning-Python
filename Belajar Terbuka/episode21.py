#Episode 21 - IF dan ELSE statement
# untuk mengatur flow dan program yang dibuat
# biasanya program satu alur, yang akan dipelajar kali ini akan akan bercabang (yes,no)

# 1. IF STATEMENT
# yang dibutuhkan:
# IF
# KONDISI
# AKSI

pertanyaan= input("sudah makan belom?")
#print(pertanyaan)
#if kondisi : aksi

#kondisi:
# a. Program if inline
#if pertanyaan == "sudah" :
    #print("wah cepet juga kamu makannya")
#else:
   #print("oh, jangan lupa makan ya!")

# b. Program if indentation
#if pertanyaan == "sudah" :
    #print("Wah cepet juga kamu makannya")
    #print("Enak dong, aku belum")
#else:
    #print("oh oke, jangan lupa makan ya!")

print(10*"=", "ELSE STATEMENT",10*"=")
# 2. ELSE STATEMENT
if pertanyaan == "sudah" :
    print("wah cepet juga kamu makannya")
else:
    print("oh, jangan lupa makan ya!")

print("END")
