kaos = 1000
kemeja = 1500
jas = 5000
jaket = 2000
kerudung = 1000
c_kolor = 1000
c_jeans = 3000
rok = 2000
daleman = 500
gamis = 5000
baju_wanita = 2000

print("DAFTAR HARGA LAUNDRY")
print('Harga kaos:',kaos,'Harga kemeja:',kemeja)
print('Harga jas:',jas,'Harga jaket:',jaket)
print('Harga kerudung:',kerudung,'Harga celana kolor:',c_kolor)
print('Harga celana jeans:',c_jeans,'Harga rok:',rok)
print('Harga daleman:',daleman,'Harga gamis:',gamis)
print('Harga baju wanita:',baju_wanita)

print("Isilah apa saja dan berapa yang mau di cuci")
in_kaos = int(input("Kaos :"))
in_kemeja = int(input("Kemeja : "))
in_jas = int(input("jas:"))
in_jaket = int(input("jaket:"))
in_kerudung = int(input("kerudung:"))
in_c_kolor = int(input("celana kolor:"))
in_c_jeans = int(input("celana jeans:"))
in_rok = int(input("rok:"))
in_daleman = int(input("daleman :"))
in_gamis = int(input("gamis:"))
in_baju_wanita = int(input("baju wanita:"))

h_kaos = kaos * in_kaos
h_kemeja = kemeja * in_kemeja
h_jas = jas * in_jas
h_jaket = jaket * in_jaket
h_c_kolor = c_kolor * in_c_kolor
h_c_jeans = c_jeans * in_c_jeans
h_rok = rok * in_rok
h_daleman = daleman * in_daleman
h_gamis = gamis * in_gamis
h_baju_wanita = baju_wanita * in_baju_wanita

print('kaos :', in_kaos)
print('kemeja :',in_kemeja)
print('jas :', in_jas)
print('jaket :', in_jaket)
print('kerudung :', in_kerudung)
print('celana kolor :', in_c_kolor)
print('celana jeans :', in_c_jeans)
print('rok :', in_rok)
print('daleman:', in_daleman)
print('gamis :', in_gamis)
print('baju wanita :', in_baju_wanita)

tot_harga = h_baju_wanita + h_c_jeans + h_c_kolor + h_daleman + h_gamis + h_jaket + h_jas + h_kaos + h_kemeja + h_rok

print('Total harganya cuci = Rp.',tot_harga,',-')