# episode 16 operasi dan manipulasi string (pt1)
nama1= 'Gold'
nama2= 'D'
nama3= 'Roger'
full_name=nama1+" "+nama2+" "+nama3

    #Menghitung panjang string
p=len(full_name) #len() adalah fungsi untuk menghitung panjang string
print("jumlah karakter pada nama lengkap =",str(p))

    #Menncari kata dalam string 
e = 'e'
status = e in full_name #operator in untuk mengecek apakah ada karakter/substring "d" dalam string
print("apakah ada karakter 'e' dalam nama lengkap =",str(status)) #karena dalam boolean hasilnya maka diubah dulu ke string

status = 'E' in full_name #untuk lebih singkat dapat langsung memasukan 'E' di status daripada di line sebelumnya
print("apakah ada karakter 'E' dalam nama lengkap =",str(status))
        #dapat dilihat UPPERCASE dan LOWERCASE itu dikategorikan berbeda
#bisa juga ditambhahkan not untuk mengatakan tidak ada
status = 'e' not in full_name #operator not in untuk mengatakan tidak ada karakter/substring "d" dalam string
print("apakah ada karakter 'e' dalam nama lengkap =",str(status)) #karena dalam boolean hasilnya maka diubah dulu ke string
        #hasilnya False karena memang ada karakter 'e' dalam full_name

    # Mengulang string
print("Wk"*10) #akan mengulang string "Wk" sebanyak 10 kali
#ATAU
print(10*"Wk") #sama aja hasilnya 

    #Mengakses karakter dalam string (indexing)
print("karakter pertama pada nama lengkap =",full_name[0]) #index dimulai dari 0
print("karakter terakhir pada nama lengkap =",full_name[-1]) #index negatif dimulai dari -1
            #jika minus maka akan dihitung dari belakang karakter
print("karakter ke-4 pada nama lengkap =",full_name[3])
#range dalam indexing 
print("karakter dari 1 sampai 3 pada nama lengkap =",full_name[0:3]) #pakai tanda titik dua (:) sama kayak Excel
            #hasilnya hanya akan "Gol" karena index ke-3 tidak dihitung, jadi harus +1
print("karakter dari 1 sampai 4 pada nama lengkap =",full_name[0:4])
print("karakter ke 0, 2, 4, 6, 8, dan 10 pada nama lengkap =",full_name[0:11:2]) 
            #+1 makanya index ke 11
            #[0:11:2] artinya dari index 0 sampai 10 dengan step 2

    #Item paling kecil dan paling besar
print("karakter paling kecil pada nama lengkap =",min(full_name)) 
            #paling kecil berdasarkan urutan ASCII
print("karakter paling besar pada nama lengkap =",max(full_name))
            #paling besar berdasarkan urutan ASCII


    #Operator dalam bentuk method
data = "lihat kebunku penuh dengan bunga"
print("\ndata =",data)
jumlah = data.count('u') #method count() untuk menghitung jumlah karakter/substring dalam string
print("jumlah karakter 'u' dalam data =",str(jumlah))

#Jika hasil dari perintahs status tadi adalah dalam bentuk BOOLEAN maka (objek).count dalam bentuk INTEGER

    
