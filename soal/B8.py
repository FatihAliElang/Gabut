nabung = 2_500_000
Pbunga = 16
akhir = 2_600_000

def lama(nabung, Pbunga, akhir):
    besar_bunga = akhir - nabung
    lama = (besar_bunga*1200)/(Pbunga*nabung)
    return lama

print(lama(nabung, Pbunga, akhir))