uang = 1_500_000
lama = 8
besar = 1_600_000
akhir = 1_500_000

def Pbunga(uang, lama, besar):
    hasil = besar - akhir
    Pbunga = (hasil*12)/(lama*uang)
    return Pbunga

print(Pbunga(uang, lama, besar))
