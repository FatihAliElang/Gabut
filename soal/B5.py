uang  = 2000000
lama = 7
besar = 2_105_000
akhir = 2_000_000

def Pbunga(uang, lama, besar):
    hasil = besar - akhir
    Pbunga = (hasil*12)/(lama*uang)
    return Pbunga

print(Pbunga(uang, lama, besar))