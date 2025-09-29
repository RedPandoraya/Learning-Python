#episode 13 Operasi Bitwise (dikarenakan masih belum terlalu diperlukan jadi di skip dulu)

#episode 14 operator assigtment

a=5 #ini adalah assignment biasa
print("nilai a =",a)
a += 3 #ini artinya a = a + 3 
a -= 2 #ini artinya a = a - 2
a *= 2 #ini artinya a = a * 2
a /= 2 #ini artinya a = a / 2
a //= 2 #ini artinya a = a // 2 (pembagian dibulatkan ke bawah)
a %= 2 #ini artinya a = a % 2 (sisa bagi)
a **= 3 #ini artinya a = a ** 3 (pangkat)
print("nilai a setelah di operasikan =",a)

#operator assignment juga bisa digunakan pada operasi bitwise
a = True
a|= False #ini artinya a = a | False (OR)
print("\nnilai a dengan True OR False =",a)
a = False
a|= False #ini artinya a = a | False (OR)
print("\nnilai a dengan False OR False =",a)

a = True
a&= False #ini artinya a = a & False (AND)
print("\nnilai a dengan True AND False =",a)
a = True
a&= True #ini artinya a = a & False (AND)
print("\nnilai a dengan True AND True =",a)

a = True
a^= False #ini artinya a = a ^ False (XOR)
print("\nnilai a dengan True XOR False =",a)
a = True
a^= True #ini artinya a = a ^ False (XOR)
print("\nnilai a dengan True XOR True =",a)

#geser kiri dan kanan (>> kanan) (<< kiri)

a = 0b0001 #ini adalah bilangan biner 1
print("\nnilai a =", format(a, '04b'))
a <<= 2 #geser kiri 2 kali
print("nilai a geser kiri 2 kali =", format(a, '04b'))
a >>= 2 #geser kanan 2 kali
print("nilai a geser kanan 2 kali =", format(a, '04b'))
