"""
PROGRAM KASIR SEDERHANA
"""

#database barang
barang = [
    {
        "id":0,
        "nama":"indomie",
        "harga":3000
    },
    {
        "id":1,
        "nama":"Telur Ayam Ras",
        "harga":2000
    }
]

#fungsi input data barang
def addBarang():
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang : "))
    print("\nPenabahan barang baru, ", nama, " yang harganya ", harga)
    confirm = input("\nLanjut : (y/n) ")
    if confirm == "y":
        barang.append({
            "id":barang[len(barang)-1]["id"]+1,
            "nama":nama,
            "harga":harga
        })
        print("\nDone Bos,...!!")
    elif confirm == "n":
        addBarang()
    else:
        exit()

#fungsi hapus data barang
def removeBarang():
    daftarBarang()
    select = int(input("\nMasukkan nomor ID barang : "))
    barangTerpilih = [x for x in barang if x["id"] == select][0]
    confirm = input(str(barangTerpilih["nama"]) + "akan dihapus? (y/n)")
    if confirm == "y":
        barang.remove(barangTerpilih)
        print("Barang berhasil dihapus")
    elif confirm == "y":
        removeBarang()
    else:
        exit()

#fungsi menampilkan data barang
def daftarBarang():
    print("\nID", " "*3, "Nama Barang")
    for i in range(len(barang)):
        print(barang[i]["id"], " "*3, barang[i]["nama"])

#fungsi menghitung data belanja
def belanja():
    print("\nMau beli apa,...??")
    totalHarga = 0
    while True:
        daftarBarang()
        print("*Kalo sudah cukup, ketik 99")
        opsi = int(input("Masukkan ID barang: "))
        if opsi == 99:
            break
        jumlahBarang = int(input("Mau beli berapa: "))
        selected = [x for x in barang if x["id"] == opsi][0]
        harga = selected["harga"]*jumlahBarang
        totalHarga += harga
        print(totalHarga)
    print("\nTotal pembayaran adalah ", totalHarga)

#fungsi menu
def menu():
    a = ["Belanja", "Tambahkan Barang", "Hapus Barang"]
    print("\n-----MENU-----")
    for i in range(len(a)):
        print(i, a[i])
    b = int(input("Pilih opsi: "))
    if b < len(a):
        if b == 0:
            belanja()
        elif b == 1:
            addBarang()
        elif b == 2:
            removeBarang()
        else:
            exit()

#run program
while True:
    menu()
