def mulai():
    print("Tolong memilih operasi apa yang ingin dijalankan:")
    print("A untuk penambahan, B untuk pengurangan, C untuk Perkalian, D untuk Pembagian, E untuk Pangkat: ")
    operasi = str(input("Masukkan pilihan: ")).upper()

    angka_1 = int(input('Masukkan angka pertama: '))
    angka_2 = int(input('Masukkan angka kedua: '))

    if operasi == 'A':
        print(angka_1, "+", angka_2, "=")
        print(angka_1 + angka_2)

    elif operasi == 'B':
        print(angka_1, "-", angka_2, "=")
        print(angka_1 - angka_2)

    elif operasi == 'C':
        print(angka_1, "x", angka_2, "=")
        print(angka_1 * angka_2)

    elif operasi == 'D':
        print(angka_1, ":", angka_2, "=")
        print(angka_1 / angka_2)

    elif operasi == 'E':
        print(angka_1, "pangkat", angka_2, "=")
        print(angka_1 ** angka_2)

    else:
        print("Tolong pilih dengan benar")

    print("Apakah kamu mau memulai program lagi?")
    print("Iya atau Tidak?")
    jawab = str(input("")).lower().capitalize()

    if jawab == 'Iya':
        mulai()
    elif jawab == "Tidak":
        print("Terimakasih")
    else:
        print("Pilih dengan benar")

mulai()