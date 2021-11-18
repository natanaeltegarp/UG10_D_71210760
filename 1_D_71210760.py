hmak=int(input("Harga makanan sebesar Rp "))
hsnac=int(input("Harga snack sebesar Rp "))
hmin=int(input("Harga Minuman sebesar Rp "))
uang=int(input("Uang yang anda bawa sebesar Rp "))
totalh=hmak+hsnac+hmin

print("Total yang harus anda bayar sebesar Rp ", totalh)
if totalh<uang:
    print("Anda memiliki kembalian sebesar Rp ", uang-totalh)
elif totalh==uang:
    print("Uang anda pas! Tidak ada kembalian dan Utang :D")
else:
    print("Uang Anda kurang! Anda memiliki utang sebesar Rp ", totalh-uang)