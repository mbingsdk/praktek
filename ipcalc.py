"""
Test IP Calculaor
"""

ipAddress = input("Masukkan IP Address: ") #"192.168.1.1/16"

r8bit = list(range(128, 256))

#Menentukan kelas Network ID:
def kelas(ip):
    ret = None
    netId = int(ip.split(".")[0])
    if netId in range(0, 128):
        ret = "A"
    elif netId in range(128, 192):
        ret = "B"
    elif netId in range(192, 224):
        ret = "C"
    elif netId in range(224, 240):
        ret = "D"
    elif netId in range(240, 255):
        ret = "E"
    return ret

#Menentukan Netmask dan Binary
def subnet(ip):
    CIDR = int(ip.split("/")[1])
    n = CIDR//8
    xbin = ""
    ret = ""
    for i in range(4):
        for j in r8bit:
            b = bin(j).replace("0b", "")
            if i < n:
                if b.count("1") == 8:
                    xbin += b+"."
                    ret += str(j)+"."
                    CIDR -= 8
                    break
            elif "0" in b:
                if b.split("0")[0].count("1") == CIDR:
                    xbin += b +"."
                    ret += str(j)+"."
                    CIDR -= b.split("0")[0].count("1")
                    break
            else:
                if i < 3:
                    xbin += "0"*8+"."
                    ret += "0."
                else:
                    xbin += "0"*8
                    ret += "0"
    return xbin, ret

#Menentukan Range IP dan Jumlah Host
def rangeIP(ip):
    CIDR = int(ip.split("/")[1])
    s = 32-CIDR
    totalHost = (2**s)-2
    sp = CIDR//8
    netmask = subnet(ip)[1].split(".")
    netID = ".".join(ip.split(".")[0:sp])
    ipStart = ""
    ipEnd = ""
    n = 0
    total = 0
    for i in ip.split("/")[0].split("."):
        if n >= sp:
            if n < 3:
                st = "0"
                en = str(255-int(netmask[n]))
            else:
                st = "1"
                en = str(254-int(netmask[n]))
            if netID not in ipStart:
                ipStart += netID + "." + st
                ipEnd += netID + "." + en
            else:
                ipStart += "." + st
                ipEnd += "." + en
        n += 1
    return ipStart, ipEnd, totalHost

#Testing output
print("IP Kelas:", kelas(ipAddress))
print("Netmask:", subnet(ipAddress)[1])
print("Range IP:", f"{rangeIP(ipAddress)[0]}-{rangeIP(ipAddress)[1]}")
print("Total Host:", rangeIP(ipAddress)[2])
