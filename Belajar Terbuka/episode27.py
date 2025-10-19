# Episode 27 Break
# Break adalah untuk menghentikan perulangan (loop) secara paksa pada kondisi tertentu

data_int = int(input("Masukkan angka= "))
a=0
while True:  #perulangan tanpa henti
    a+=1
    print(f"angka pada saat ini= {a}")

    if a== data_int:
        print("Berhenti")
        break  #jika a=3 maka perulangan akan dihentikan selelah mengeksekusi perintah break
    print("apa kabar?")
print("selesai")