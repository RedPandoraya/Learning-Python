#operasi logika/boolean

#menggunakan NOT, OR, AND, XOR

#NOT (kebalikan)
print("\n==============NOT==============")
a = False
c = not a
print("nilai a adalah = ",a)
print("nilai c adalah = ",c)

#OR (jika salah satu True, maka hasilnya True)
print("\n==============OR==============")
a = False
b = True
c = a or b
print("False OR TRUE = ",c)
a = False
b = False
c = a or b
print("False OR False = ",c)

#AND (jika salah satu False, maka hasilnya False)
print("\n==============AND==============")
a = False
b = True
c = a and b
print("FALSE AND True = ",c)
a = True
b = True
c = a and b
print("True AND True = " ,c)


#XOR 
#jika salah satu ada yang True, maka hasilnya akan True, sisanya False
#beda dengan OR, jika kedua nilai True, maka hasilnya False
print("\n==============XOR==============") #uniknya disini XOR memakai tanda ^
a = False
b = True
c = a ^ b
print("FALSE XOR True = ",c)
a = False
b = False
c = a ^ b
print("False XOR False = " ,c)
a = True
b = True
c = a ^ b
print("True XOR True = " ,c)