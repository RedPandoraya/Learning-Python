# Episode 19 - String Width and Alignment

# Width and Multiline
nama="Red Panda"
panggilan="Panda"
umur= "10"
tinggi= "160"
fav_number= 7

# String standar
biodata= f"Nama lengkap= {nama}, Nama panggilan= {panggilan}, Umur= {umur}, Tinggi= {tinggi}cm, Angka favorit= {fav_number}"
print("\nBIODATA DENGAN STRING STANDAR\n", biodata)

# String Multiline (dengan menggunakan multiline (\n), atau dengan menggunakan 3x tanda double quote("""))
biodata= f"Nama lengkap= {nama},\n Nama panggilan= {panggilan},\n Umur= {umur},\n Tinggi= {tinggi}cm,\n Angka favorit= {fav_number}"
print('\nBIODATA DENGAN \\n', biodata)

biodata= f"""
Nama lengkap    = {nama}
Nama panggilan  = {panggilan}
Umur            = {umur}
Tinggi          = {tinggi}cm
Angka favorit   = {fav_number}"""
#Jika menggunakan 3x double quote maka harus diatur sendiri linenya
print('\nBIODATA DENGAN MENGGUNAKAN 3x DOUBLE QUOTE (")', biodata)


# Mengatur Lebar
biodata= f"""
Nama lengkap    = {nama:>10}
Nama panggilan  = {panggilan:>10} 
Umur            = {umur:>10}
Tinggi          = {tinggi:>7} cm 
Angka favorit   = {fav_number:>10}"""
#Jika memakai :>10 maka akan rata kanan, 10 artinya sediakan ruang setidaknya 10 karakter
#Alasan kenapa di tinggi hanya 7 karena space " " dan cm udah termasuk 3 kata, jadi 10-3=7
print("\nBIODATA DENGAN :>10", biodata)