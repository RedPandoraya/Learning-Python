#episode 10  operasi komparasi

#hasil dari komparasi adalah boolean (True/False)

#lebih dari (>)
#kurang dari (<)
#lebih dari sama dengan (>=)
#kurang dari sama dengan (<=)
#sama dengan (==)
#tidak sama dengan (!=)

#is (apakah sama objectnya)
#is not (apakah tidak sama objectnya)

a = 10
kurdar= a < 15
print("10 kurang dari 15 = ", kurdar) #True

lebdar= a > 10
print("10 lebih dari 10 = ", lebdar) #False

lebdarsam= a >= 10 
print("10 lebih dari sama dengan 10 = ", lebdarsam) #True

kurdarsam= a <= 9
print("10 kurang dari sama dengan 9 = ", kurdarsam) #False

sama= a == 10
print("10 sama dengan 10 = ", sama) #True  

tidaksama= a != 9 #intinya jika angkanya tidak sama maka hasilnya True
print("10 tidak sama dengan 9 = ", tidaksama) #True
tidaksama= a != 10
print("10 tidak sama dengan 10 = ", tidaksama) #False

#operasi komparasi di atas sama dengan matematika biasa

#is dan is not
#gunanya is dan is not adalah untuk membandingkan object
a = 10
b = 10
print(a is b) #True karena objectnya sama
print(a is not b) #False karena objectnya sama
c = 5
print(a is c) #False karena objectnya tidak sama
print(a is not c) #True karena objectnya tidak sama