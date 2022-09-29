pinjam = 5_000_000
bunga = 10
waktu = 2

def cicil(pinjam, bunga, waktu):
    besar_bunga = waktu*(bunga/100)*pinjam
    kembali = pinjam + besar_bunga
    bulan = waktu * 12
    cicil = kembali/bulan
    return cicil

print(cicil(pinjam, bunga, waktu))
    