# Coba
x = 0

while (x < 10):
    x += 1
    print("looping ke-"+str(x))
       
for i in range(2, 12, 2):
    print("looping ke-"+str(i))


# Piramida
def piramida():
    a = int(input('Pilih tinggi piramida: '))
    b = a

    for i in range(a):
        for j in range(i, a):
            print(" ", end="")
        b-= 1
        for k in range(b, a):
            print("* ", end="")
        print("")
    
    print("Lagi?")
    lagi = str(input("y/n: ")).lower()
    if lagi == "y":
        piramida()

    else:
        print("Terima kasih")

piramida()


# Berlian beku
tinggi = eval(input("Pilih tinggi berlian: "))

for m in range(tinggi):
    print(" " * (tinggi - m), "0" * (2*m + 1))
for m in range (tinggi - 2, -1, -1):
    print(" " * (tinggi - m), "0" * (2*m +1))
