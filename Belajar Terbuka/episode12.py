#episode 12 latihan komparasi dan logika (eps9 dan eps10)

#membuat gabungan area rentang dan angka

#+ = True
#- = False

#+++3---10+++ (kurang dari 3 atau lebih dari 10)
##inputuser=float(input("masukkan angka kurang dari 3 atau lebih dari 10 = "))
#dipecah dan digabungkan
##kurdar= inputuser < 3 #kurang dari 3
##lebihdar= inputuser > 10 #lebih dari 10
#digabungkan dengan OR
##hasil= kurdar or lebihdar
##print("hasilnya adalah = ",hasil)

#---3+++10--- (lebih dari 3 dan kurang dari 10)
##inputuser=(float(input("masukkan angka lebih dari 3 dan kurang dari 10 = ")))
#dipecah dan digabungkan
##lebdar= inputuser > 3 #lebih dari 3
##kurdar= inputuser < 10 #kurang dari 10
#digabungkan dengan AND
##hasil= lebdar and kurdar
##print("hasilnya adalah = ",hasil)


#PR
#---0+++5---8+++11--- (lebih dari 0 dan kurang dari 5 ATAU lebih dari 8 dan kurang dari 11)
inputuser=float(input("masukkan angka lebih dari 0 dan kurang dari 5 ATAU lebih dari 8 dan kurang dari 11 = "))

#lebih dari 0 dan kurang dari 5
lebdar0 = inputuser > 0
kurdar5 = inputuser < 5
hasil1 = lebdar0 and kurdar5
#lebih dari 8 dan kurang dari 11
lebdar8 = inputuser > 8
kurdar11 = inputuser < 11
hasil2 = lebdar8 and kurdar11
#digabungkan dengan OR
hasil = hasil1 or hasil2
print("hasilnya adalah = ",hasil)


#+++0---5+++8---11+++ (kurang dari 0 dan lebih dari 5 atau kurang dari 8 dan lebih dari 11)
inputuser=float(input("masukkan angka kurang dari 0 dan lebih dari 5 atau kurang dari 8 dan lebih dari 11 = "))
#kurang dari 0 dan lebih dari 5
#menggunakan OR untuk menggabungkan karena jika pakai AND nanti jika digabung hasilnya aneh
kurdar0= inputuser < 0
lebdar5 = inputuser > 5
hasil1 = kurdar0 or lebdar5
#kurang dari 8 dan lebih dari 11
kurdar8 =  inputuser <8
lebdar11= inputuser >11
hasil2 = kurdar8 or lebdar11
#digabungkan dengan OR
hasil = hasil1 and hasil2
print("hasilnya adalah = ",hasil)
