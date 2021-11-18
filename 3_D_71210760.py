dftbel=input("Masukkan daftar belanjaan Anda : ")
dftbel=dftbel.title()
print("Daftar belanja : ", dftbel.split(", "))
tambah=input("Masukkan barang yang ingin ditambahkan : ")
if tambah.title() not in dftbel:
    tambah=tambah.upper()
    dftbel=dftbel.split(", ")
    dftbel.append(tambah)
    print("Hasil penambahan pada daftar belanja : ", dftbel)
else:
    tambah=tambah.upper()
    print("Barang ", tambah, "Sudah berada dalam daftar belanja.")