# def cek(usia):
#     if (usia < 0 or usia > 100):
#         print("Usia tidak valdi")
#     elif(usia > 17):
#         print("Silahkan menonton anu")
#     else:
#         print("Silahkan menonton berlian beku")

# cek(100)

try:
    def nilai():
        x = float(input("Masukkan nilai yang didapat: "))

        if (x < 0 or x > 100):
            print("Nilai tidak valid")
        elif (x < 60):
            print("E")
        elif (x < 70):
            print("D")
        elif (x < 80):
            print("C")
        elif (x < 90):
            print("B")
        elif (x <= 100):
            print("A")

        print("Convert lagi?")
        print("Iya atau Tidak?")
        jawab = str(input("")).lower().capitalize()

        if jawab == 'Iya':
            nilai()
        elif jawab == "Tidak":
            print("Terimakasih")
        else:
            print("Pilih dengan benar")

    nilai()

except ValueError:
    print("Ketik angka")
    nilai()

