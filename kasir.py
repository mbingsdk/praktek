"""
PROGRAM KASIR SEDERHANA
"""

#Module
#import json
#from os.path import exists as fileExists
from funcATM import *

#Nama Comersial
namanya = "ALVA MARK"

#database barang
barang = [
    {
        "id":0,
        "nama":"indomie",
        "stock":50,
        "harga":3000
    },
    {
        "id":1,
        "nama":"Telur Ayam Ras",
        "stock":70,
        "harga":2000
    }
]

#fungsi input data barang
def addBarang():
    nama = input("Masukkan nama barang: ")
    juml = int(input("Jumlah barang: "))
    harga = int(input("Masukkan harga barang : "))
    print("\nPenabahan barang baru, ", nama, " yang harganya ", harga)
    confirm = input("\nLanjut : (y/n) ")
    if confirm == "y":
        barang.append({
            "id":barang[len(barang)-1]["id"]+1,
            "nama":nama,
            "stock":juml,
            "harga":harga
        })
        print("\nDone Bos,...!!")
    elif confirm == "n":
        addBarang()
    else:
        exit()
    saveData(barang, "gudang.json")
        
#fungsi tambah stock
def tambahStock():
    daftarBarang()
    select = int(input("\nMasukkan nomor ID barang : "))
    juml = int(input("Berapa banyak: "))
    barangTerpilih = [x for x in barang if x["id"] == select][0]
    confirm = input(str(barangTerpilih["nama"]) + "akan ditambah? (y/n)")
    if confirm == "y":
        barangTerpilih["stock"] += juml
        print("Stock sudah ditambah")
    elif confirm == "n":
        pass
    else:
        exit()
    saveData(barang, "gudang.json")

#fungsi hapus data barang
def removeBarang():
    daftarBarang()
    select = int(input("\nMasukkan nomor ID barang : "))
    barangTerpilih = [x for x in barang if x["id"] == select][0]
    confirm = input(str(barangTerpilih["nama"]) + "akan dihapus? (y/n)")
    if confirm == "y":
        barang.remove(barangTerpilih)
        print("Barang berhasil dihapus")
    elif confirm == "n":
        pass
    else:
        exit()
    saveData(barang, "gudang.json")

#fungsi menampilkan data barang
def daftarBarang():
    print("\nID", " "*3, "Nama Barang", " "*3, "Harga")
    for i in range(len(barang)):
        print(barang[i]["id"], " "*3, barang[i]["nama"], rp(barang[i]["harga"]))

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
        if jumlahBarang <= selected["stock"]:
            harga = selected["harga"]*jumlahBarang
            totalHarga += harga
            print("-"*25)
            print("\nTotal saat ini :", rp(totalHarga))
            selected["stock"] -= jumlahBarang
        else:
            print("Stock barang tidak cukup!")
    print("\nTotal pembayaran adalah ", rp(totalHarga))
    pembayaran(totalHarga)

#Pembayaran
def pembayaran(total):
    print()
    print("Pilih metode pembayaran")
    pemb = ["CASH", "ATM"]
    for i in range(len(pemb)):
        print(i, pemb[i])
    ops = int(input("-> "))
    if ops < len(pemb):
        if ops == 0:
            uang = int(input("Bayar berapa: "))
            if uang >= total:
                print()
                print("="*25)
                print("|| Total :", rp(total))
                print("|| Bayar :", rp(uang))
                print("-"*25)
                print("|| Kembali :", rp(uang-total))
                print("="*25)
            else:
                print("Uang anda tidak cukup!")
        elif ops == 1:
            pembayaranToko(total)
        else:
            print("Salah pilih bos!")
    else:
        pass
    saveData(barang, "gudang.json")

#fungsi menu
def menu():
    print()
    print("="*25)
    print("|| Welcome to" namanya)
    print("|| Semoga Anda Bukan Maling")
    print("="*25)
    a = ["Belanja", "Tambahkan Barang", "Hapus Barang", "Tambah Stock"]
    print("\n\n-----MENU-----")
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
        elif b == 3:
            tambahStock()
        else:
            exit()

#Loading database
if fileExists('gudang.json'):
    barang = loadData("gudang.json")
else:
    print("database file not exists")

#run program
while True:
    menu()
