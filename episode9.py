#episode 9 latihan perhitungan sederhana
#program konversi suhu

celcius=float(input("suhu dalam celcius= "))
print("suhu= ", celcius, "celcius")

#mengubah celcius ke reamur
reamur=(4/5)*celcius
print("suhu dalam reamur= ", reamur, "reamur")

#mengubah celcius ke fahrenheit
fahrenheit=(9/5)*celcius+32
print("suhu dalam fahrenheit= ", fahrenheit, "fahrenheit")

#mengubah celcius ke kelvin
kelvin=celcius+273
print("suhu dalam kelvin= ", kelvin, "kelvin")

print("\n================================\n")
#PR
# 1. konversi suhu dari fahreinheit ke kelvin
# 2. konversi suhu dari kelvin ke fahreinheit

#jawaban no 1
fahreinheit=(float(input("suhu dalam fahreinheit= ")))
kelvin=(5/9)*(fahreinheit-32)+273
print("suhu dalam kelvin= ", kelvin, "kelvin") 

#jawaban no 2
kelvin=(float(input("suhu dalam kelvin= ")))
fahreinheit=(kelvin-273)*(9/5)+32
print("suhu dalam fahreinheit= ", fahreinheit, "fahreinheit")

