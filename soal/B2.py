Pbunga = 16
lama = 90
besar = 400000

def tabungan(besar, lama, Pbunga):
    tabungan = lama/360 * Pbunga/100
    uang = besar/tabungan
    return uang

print(tabungan(besar, lama, Pbunga))

