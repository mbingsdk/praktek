import requests

key = input("Masukkan nama bintang: ")
hm = requests.get("https://api.vx6-ct.com/zodiak.php", params={'key':key})
p = hm.json()

for i in p:
    print(i.upper(), ":", p[i], "\n")")
