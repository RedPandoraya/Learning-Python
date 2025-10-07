# akan memakai library Date, time jadi harus diimport dulu
# sebelum itu harus diinstal dulu di terminal : pip install datetime, baru :
import datetime as dt

hari_ini= dt.date.today()
print(hari_ini)
print(f'hari ini adalah hari= {hari_ini:%A}')

lahir = dt.date (2000,12,20)
print(lahir)
print(f'Pada tanggal 20, bulan, tahun 2000 adalah hari= {lahir:%A}')

# Mencoba membuat pendeketsi hari lahir
print("Masukkan tanggal, bulan, dan tahun lahir anda: ")
d= int(input("Tanggal\t: "))
m= int(input("Bulan\t: "))
y= int(input("Tahun\t: "))
#casting ke int agar bisa diakai datetime

tgl= dt.date(y,m,d)
print(f"Tanggal, bulan, dan tahun: {tgl}")
print(f"Pada hari: {tgl:%A}")

# Menghitung umur
hari_ini= dt.date.today()
print(f"Hari ini tanggal {hari_ini}")
umur= hari_ini - tgl
# print(f"Umur pada saat ini: {umur}")
# Jika dihitung seperti ini, maka hasilnya akan dalam bentuk hari (9057days)

# Maka dapat dilakukan seperti ini untuk mendapat hasil dalam bentuk tahun :
umur_tahun= umur.days//366 #Floor division
print(f"Umur pada saat ini= {umur_tahun} tahun")

# Jika ingin dapat bulan lahirnya:
umur_bulan= (umur.days%365)//30
#           sisa pembagian,  dibagi 30
print(f"Umur pada saat ini: {umur_tahun} tahun, pada bulan: {umur_bulan}")
