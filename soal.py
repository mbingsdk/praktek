"""
Soal Python3
Source : w3school.com
"""

import base64, random

def enc(text):
    text = base64.b64encode(text.encode('ascii')).decode('ascii')
    return text

def dcd(text):
    text = base64.b64decode(text.encode('ascii')).decode('ascii')
    return text

print()
print("="*25)
print("SOAL-PYTHON")
print("="*25)
print()

data = {
    "soal":[
        "Menampilkan output Hello World",
        "Penulisan Komentar dalam Python!",
        "Cara penulisan Variable yang salah!",
        "Membuat variable Integer yang berisi angka 5!",
        "Extensi file yang digunakan untuk bahasa Python!",
        "Membuat variable bilangan pecahan yang berisi 2.8!",
        "Syntax untuk mengecek/menampilkan type data!",
        "Membuat Function/fungsi!",
        "Return 'Hello' == \"Hello\"!",
        "Menampilkan karakter pertama dalam string!",
        "Menghapus spasi/tab di awal dan di akhir string!",
        "Mengubah huruf text menjadi Balok!",
        "Mengganti salah satu atau beberapa karakter dalam string!",
        "Operator yang digunakan untuk menduplikasi string!",
        "Operator yang digunakan dalam perbandingan kesamaan!",
        "Contoh struktur data List!",
        "Contoh struktur data Tuple",
        "Contoh struktur data Set",
        "Contoh struktur data Dictionary",
        "Yang termasuk struktur data yang bisa di ubah dan bisa berisi data duplikat/ganda!",
        "Struktur data yang tidak bisa berisi data duplikat!",
        "Contoh penulisan awal yang benar untuk kondisi if!",
        "Contoh awalan while Loop!",
        "Contoh awalan for Loop!",
        "Yang digunakan untuk menghentikan Looping!"
    ],
    "jawaban":[
        ["print(\"Hello World\")","p(\"Hello World\")","echo(\"Hello World\");","echo \"Hello World\""],
        ["#This is a comment","/*This is a comment*/","//This is a comment"],
        ["my_var","_myvar","Myvar","my-var"],
        ["x = 5","x = int(5)", "Semua jawaban benar"],
        [".py",".pyt",".pt",".pyth"],
        ["x = 2.8","Semua jawaban benar","x = float(2.8)"],
        ["print(type(x))","print(typeOf(x))","print(typeof x )","print(typeof(x))"],
        ["def myFunction():","function myFunction():","create myFunction():"],
        ["True","False"],
        ["x = \"Hello\"[0]","x = \"Hello\".sub(0, 1)","x = sub(\"Hello\", 0, 1)"],
        ["strip()","len()","ptrim()","trim()"],
        ["upper()","toUpperCase()","uppercase()","upperCase()"],
        ["replace()","replaceString()","repl()","switch()"],
        ["*","x","%","#"],
        ["==","><","=","<>"],
        ["[\"apple\", \"banana\", \"cherry\"]","{\"apple\", \"banana\", \"cherry\"}","(\"name\": \"apple\", \"color\": \"green\")","{\"apple\", \"banana\", \"cherry\"}"],
        ["(\"apple\", \"banana\", \"cherry\")","{\"apple\", \"banana\", \"cherry\"}","{\"name\": \"apple\", \"color\": \"green\"}","[\"apple\", \"banana\", \"cherry\"]"],
        ["{\"apple\", \"banana\", \"cherry\"}","{\"name\": \"apple\", \"color\": \"green\"}","[\"apple\", \"banana\", \"cherry\"]","(\"apple\", \"banana\", \"cherry\")"],
        ["{\"name\": \"apple\", \"color\": \"green\"}","(\"apple\", \"banana\", \"cherry\")","{\"apple\", \"banana\", \"cherry\"}","[\"apple\", \"banana\", \"cherry\"]"],
        ["LIST","TUPLE","SET","DICTIONARY"],
        ["SET","LIST","TUPLE"],
        ["if x > y:","if x > y then:","if (x > y)"],
        ["while x > y:","while (x > y)","while x > y {","x > y while {"],
        ["for x in y:","for x > y:","for each x in y:"],
        ["break","return","exit","stop"]
    ],
    "correct":["cHJpbnQoIkhlbGxvIFdvcmxkIik=","I1RoaXMgaXMgYSBjb21tZW50","bXktdmFy","U2VtdWEgamF3YWJhbiBiZW5hcg==","LnB5","U2VtdWEgamF3YWJhbiBiZW5hcg==","cHJpbnQodHlwZSh4KSk=","ZGVmIG15RnVuY3Rpb24oKTo=","VHJ1ZQ==","eCA9ICJIZWxsbyJbMF0=","c3RyaXAoKQ==","dXBwZXIoKQ==","cmVwbGFjZSgp","Kg==","PT0=","WyJhcHBsZSIsICJiYW5hbmEiLCAiY2hlcnJ5Il0=","KCJhcHBsZSIsICJiYW5hbmEiLCAiY2hlcnJ5Iik=","eyJhcHBsZSIsICJiYW5hbmEiLCAiY2hlcnJ5In0=","eyJuYW1lIjogImFwcGxlIiwgImNvbG9yIjogImdyZWVuIn0=","TElTVA==","U0VU","aWYgeCA+IHk6","d2hpbGUgeCA+IHk6","Zm9yIHggaW4geTo=","YnJlYWs="]
}

soal = data["soal"]
jawaban = data["jawaban"]
correct = data["correct"]
ops = ["a","b","c","d"]
opsi = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3
}
skor = 0
benar = {}
salah = {}

nama = input("Masukan nama: ")
print("-"*25)

for i in range(len(soal)):
    print()
    print(f"{i+1}.", soal[i])
    acak = jawaban[i]
    random.shuffle(acak)
    for j in range(len(acak)):
        print(f"    {ops[j]}.", acak[j])
    print()
    x = input("Pilih jawaban: ")
    x = acak[opsi[x]]
    if enc(x) == correct[i]:
        benar[i] = x
        skor += 4
        print("BENAR!")
    else:
        salah[i] = x
        print("SALAH!")
        #skor -= 1
    print()

print("-"*25)
print("Nama  :", nama)
print("Benar :", len(benar))
print("Salah :", len(salah))
print("Skor  :", skor)
print("="*25)
