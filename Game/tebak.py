import random as abstrak
acak = abstrak.randint(1, 100)

while True:
    print("=====Selamat Menebak=====")
    pilih = int(input("Tebak Angkanya: "))
    if(pilih < acak):
        print("Angka terlalu kecil")
    elif(pilih > acak):
        print("Angka terlalu besar")
    else:
        print("Tebakan anda benar")
        break