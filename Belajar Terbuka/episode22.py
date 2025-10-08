#Episode 22 - ELIF Statement
# atau bisa juga dikatakan ELSE IF Statement

#IF  ...(kondisi1)
#    ...(aksi)
#ELSE...(kondisi2)
#    ...(aksi)
#ELSE...(kondisi3)
#    ...(aksi)


pertanyaan= input("sudah makan belum?")

if pertanyaan =="sudah" #kondisi1
    print("cepat juga kamu makannya") #aksi true 1
else pertanyaan == "belum" #kondisi2
    print("makan dong, emangnya kamu ga lapar") #aksi true 2
else pertanyaan:
    print("eh, sorry bang, kirain temen gw")

# kondisi elif bisa ditambah sampai berapapun

