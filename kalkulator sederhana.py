bil1 = int(input("Masukan bilangan 1:"))
bil2 = int(input("Masukan bilangan 2: "))

print("Pilih Operasi = 1.Tambah 2.Kurang 3.Bagi 4.Kali")

operasi = int(input(""))

tambah = bil1 + bil2
kurang = bil1 + bil2
bagi = bil1 / bil2
kali = bil1 * bil2

if operasi==1:
    print("Hasilnya adalah", tambah)
elif operasi==2:
    print("Hasilnya adalah", kurang)
elif operasi==3:
    print("Hasilnya adalah", bagi)
elif operasi==4:
    print("Hasilnya adalah", kali)
else:
    print("Salah Pilih Operasi")
