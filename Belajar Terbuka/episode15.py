#episode 15 pengenalan string

#seperti yang sudah diketahui string adalah kumpulan dari karakter
string = "ini adalah string"


#Ada beberapa cara untuk membuat string
    #1. dengan menggunakan tanda petik satu (') (single quote)
    #2. dengan menggunakan tanda petik dua (") (double quote)
    #3. dengan menggunakan tanda petik tiga (''' atau """)
#bisa double quote atau single quote dan hasilnya nanti akan menjadi direct dialog

#Ada beberapa tanda yang bisa digunakan di dalam string
    #1. \n untuk membuat baris baru (new line/enter)
newline="ini adalah baris pertama\nini adalah baris kedua"
print(newline)
    #2. \t untuk membuat tab (tabulasi)
tab="ini adalah kata pertama\tini adalah kata kedua"
print(tab)
    #3. \\ untuk membuat karakter backslash (\)
backslash="ini adalah karakter backslash \\"
print(backslash)
    #4. \b untuk menghapus karakter sebelumnya (backspace)
backspace="ini adalah kata yang salah\b" #akan menghapus karakter 'h'
print(backspace)
    #5. \r untuk mengembalikan kursor ke awal baris (carriage return)
carriagereturn="ini adalah kata yang salah\rbenar"
print(carriagereturn) #kata terakhir (benar) akan menimpa kata "ini"


#Bisa juga jika dalam string ingin menggunakan banyak backslash
path = "C:\\User\\Admin\\Documents\\file.txt" #agak ribet, jadi ada alternatif lain
print("\npath dengan double backslash =",path)
#dengan menggunakan Literal String / raw string
path = r"C:\User\Admin\Documents\file.txt" #dengan menambahkan huruf r di depan string
print("\npath dengan raw string =",path)

#literal string juga bisa digabungkan dengan multiline string atau raw string
multilinepath = r"""C:\User\Admin\Documents\file.txt
Folder1\Folder2\Folder3"""
print("\nmultiline path dengan raw string =",multilinepath)
#jadi tidak perlu menambahkan \n untuk membuat baris baru
