#input
#menentukan luas keramik
panjang = 25 #cm
lebar = 20 #cm
luas_teras = 20 
#proses mencari luas keramik dan mencari keramik yang dibutuhkan
luas_keramik = panjang*lebar/10000 #dibagi 10000 agar yang semula adalah cm menjadi m
butuh = luas_teras/luas_keramik
print(butuh)
