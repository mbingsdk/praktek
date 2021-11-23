"""
KONSEP PROGRAM APLIKASI ATM
"""

namaATM = "ATM BRO Bersarang"

#Database
database = {
    "dataRekening":{
        "123456":{
            "nama":"NUR ALMAIDA",
            "rek":"12341234",
            "pin":"123456",
            "saldo":20000000
        }
    }
}

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
    opsi = input("Pilih nomor urut: ")
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
        menu(dataUser)

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
    nominal = input("Masukkan jumlah yang mau dikirim: ")
    if database["dataRekening"][dataUser["pin"]]["saldo"] >= nominal:
        database["dataRekening"][pin]["saldo"] += nominal
        database["dataRekening"][dataUser["pin"]]["saldo"] -= nominal
        print("Transfer berhasil!")
        print("Semoga uangnya bukan hasil korupsi!")
    else:
        print("Periksa saldomu dulu bos!")
        transfer(dataUser)

#Penarikan
def penarikan(dataUser):
    print()
    n = input("Mau minta berapa: ")
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
    n = input("Jumlah yang setor: ")
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
    pass

client = auth()
while True:
    menu(dataUser)
