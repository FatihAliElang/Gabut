#Input
Pbunga = 12/100
uang = 1000000
lama = 6

#proses
def bunga(Pbunga, uang, lama):
    bunga = lama/12 * Pbunga * uang
    return bunga

#output
print(bunga(Pbunga, uang, lama))