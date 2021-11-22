"""
PROGRAM KASIR
"""

#Database
dataBarang = [
    {
        "id":0,
        "nama":"Indomie",
        "harga":3000
    },
    {
        "id":1,
        "nama":"Shampo",
        "harga":1000
    }
]

#Penambahan Barang
def addBarang():
    print("<|| PENAMBAHAN DAFTAR BARANG")
    namaBarang = input("Nama Barang: ")
    hargaBarang = int(input("Harga: "))
    totalBarang = len(dataBarang)
    lastId = dataBarang[totalBarang-1]["id"]
    data = {
        "id":lastId+1,
        "nama":namaBarang,
        "harga":hargaBarang
    }
    dataBarang.append(data)
    print("<|| Barang Berhasil Ditambahkan!")

#Penghapusan Barang
def hapusBarang():
    daftarBarang()
    pilihan = int(input("\nPilih ID barang: "))
    pilihan = [x for x in dataBarang if x["id"] == pilihan][0]
    dataBarang.remove(pilihan)
    print("Barang Berhasil Disingkirkan!")

#Menampilkan Data Barang
def daftarBarang():
    print("\nID", " "*3, "Nama Barang", "Harga")
    for i in range(len(dataBarang)):
        print(dataBarang[i]["id"], " "*3, dataBarang[i]["nama"], dataBarang[i]["harga"])

#Data Belanja
def belanja():
    daftarBarang()
    idBarang = int(input("Pilih ID barang: "))
    jumlahBarang = int(input("Mau beli berapa banyak: "))
    detailBarang = [x for x in dataBarang if x["id"] == idBarang][0]
    totalHarga = detailBarang["harga"] * jumlahBarang
    print("Anda harus bayar sekarang atau saya bunuh, Totalnya : ", totalHarga)

#Menunya
def menu():
    a = ["Belanja", "Tambah Item", "Hapus Item"]
    for i in range(len(a)):
        print(i, a[i])
    b = int(input("Pilih nomor opsi: "))
    if b < len(a):
        if b == 0:
            belanja()
        elif b == 1:
            addBarang()
        elif b == 2:
            hapusBarang()
        else:
            exit()

while True:
    menu()
