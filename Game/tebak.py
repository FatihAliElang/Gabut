import random as abstrak
acak = abstrak.randint(1, 100)

print("=====Selamat Menebak=====")

while True:
    try:
        pilih = int(input("Tebak Angkanya: "))
        if(pilih < acak):
            print("Angka terlalu kecil")
            print("")
        elif(pilih > acak):
            print("Angka terlalu besar")
            print("")
        else:
            print("=====Tebakan anda benar=====")
            break

    except ValueError:
        print("Ketik angka")
        
           
