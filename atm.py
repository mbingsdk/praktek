"""
KONSEP PROGRAM APLIKASI ATM
"""

#Module
import random, json
from os.path import exists as file_exists

#Nama ATM
namaATM = "ATM BRO Bersarang"

#Database
database = {
    "dataRekening":{
        "123456":{
            "nama":"NUR ALMAIDA",
            "rek":"12341234",
            "pin":"123456",
            "saldo":20000000
        },
        "654321":{
            "nama":"SYAHRIL",
            "rek":"66667777",
            "pin":"654321",
            "saldo":55000000
        }
    }
}

#Load Data
def loadData():
    f = open('dataATM.json')
    data = json.load(f)
    f.close
    return data

#Backup data
def saveData(data):
    jsonString = json.dumps(data)
    f = open("dataATM.json", "w")
    f.write(jsonString)
    f.close()

#Tahap Authentication / Login
def auth():
    print()
    print("Masukkan Kartu ATM")
    pin = input("Masukkan kode PIN: ")
    daftarPin = [x for x in database["dataRekening"]]
    if pin in daftarPin:
        datanya = database["dataRekening"][pin]
    else:
        print("Kode PIN yang anda masukkan, SALAH!")
        auth()
    return datanya

#Menu
def menu(dataUser):
    print()
    print("="*20)
    print(" "*5, "Welcome to")
    print(namaATM)
    print("="*20)
    m = ["TRANSFER", "PENARIKAN", "SETOR TUNAI", "CEK SALDO", "REGISTRASI", "EXIT"]
    jumlahMenu = len(m)
    for i in range(jumlahMenu):
        print(i, m[i])
    opsi = int(input("Pilih nomor urut: "))
    if opsi == 0:
        transfer(dataUser)
    elif opsi == 1:
        penarikan(dataUser)
    elif opsi == 2:
        setor(dataUser)
    elif opsi == 3:
        saldo(dataUser)
    elif opsi == 4:
        reg(dataUser)
    elif opsi == 5:
        exit()
    else:
        login()

#Transfer
def transfer(dataUser):
    print()
    pin = ""
    nomor = input("Masukkan nomor rekening tujuan")
    for i in database["dataRekening"]:
        if database["dataRekening"][i]["rek"] == nomor:
            pin = i
            break
        else:
            pass
    if pin != "":
        nominal = int(input("Masukkan jumlah yang mau dikirim: "))
        if database["dataRekening"][dataUser["pin"]]["saldo"] >= nominal:
            database["dataRekening"][pin]["saldo"] += nominal
            database["dataRekening"][dataUser["pin"]]["saldo"] -= nominal
            print("Transfer berhasil!")
            print("Semoga uangnya bukan hasil korupsi!")
        else:
            print("Periksa saldomu dulu bos!")
            transfer(dataUser)
    else:
        print("Nomor rekening tidak terdaftar")

#Penarikan
def penarikan(dataUser):
    print()
    n = int(input("Mau minta berapa: "))
    if database["dataRekening"][dataUser["pin"]]["saldo"] >= n:
        print("krik krik kriuk dumplak dumlpak byuoar")
        print("Jangan lupa trakir bos!")
        database["dataRekening"][dataUser["pin"]]["saldo"] -= n
    else:
        print("Periksa saldomu dulu bos!")
        penarikan(dataUser)

#Setor Tunai
def setor(dataUser):
    print()
    n = int(input("Jumlah yang setor: "))
    database["dataRekening"][dataUser["pin"]]["saldo"] += n
    print("Sudah Bos!!")

#Cek Saldo
def saldo(dataUser):
    saldonya = database["dataRekening"][dataUser["pin"]]["saldo"]
    print()
    print("Jumlah saldo anda:", saldonya)
    print("Jangan Lupa Sedekah, Chips 5B")

#Registrasi
def reg(dataUser):
    print()
    print("-----FORM REGISTRASI-----")
    nama = input("Nama Lengkap: ")
    kodePin = input("Kode PIN 6 digit: ")
    if kodePin not in list(database["dataRekening"]):
        c = input("Konfirmasi Kode PIN: ")
        if c == kodePin and len(kodePin) == 6:
            rek = str(random.randint(10000000, 99999999))
            database["dataRekening"][c] = {
                "nama":nama,
                "rek":rek,
                "pin":c,
                "saldo":0
            }
            print("Masukkan saldo awal anda!")
            setor(database["dataRekening"][c])
            print()
            print("REKENING BERHASIL DIBUAT")
            for i in database["dataRekening"][c]:
                print(i.upper(), database["dataRekening"][c][i])
            menu(dataUser)
        else:
            print("Kode PIN anda Salah!")
            reg(dataUser)
    else:
        print("Gunakan kode PIN yang lain!")
        reg(dataUser)

#Load database if database file exist
if file_exists('dataATM.json'):
    database = loadData()

#Running Program
client = auth()
while True:
    menu(client)
