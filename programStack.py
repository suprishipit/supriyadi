import os

angka =[]
def push(value):
    angka.append(value)
def pop():
    print("elemen yang terakhir dihapus :",angka.pop())
def noel():
    print ("jumlah elemen pada stack :",len(angka))
def top():
    top = len(angka) -1
    if top <0 :
        print("ora enng")
    else:
        print ("elemen terakhir :",angka[top])
def isempty():
    if len(angka) == 0:
        print("true")
    else:
        print("false")
def tampilkan (angka):
    print("semua elemen :",angka)

def mainmenu():
    os.system('cls')
    print("=========================")
    print("|          stack        |")
    print("=========================")
    print("1. masukan elemen")
    print("2. elemen yang keluar")
    print("3. Cek Empty")
    print("4. Tampil elemen terakhir")
    print("5. jumlah elemen dari stack")
    print("6. tampilkan semua elemen")
    print("---------------------------")
    pilih = "y"
    while (pilih == "y"):
        pilihan = str(input(("Silakan masukan pilihan anda [1/2/3/4/5/6]: ")))
        os.system('cls')
        if (pilihan == "1"):
            os.system('cls')
            push(input("masukan nama elemen :"))
            print("elemen yang masuk :",angka)
            print("-------------------------------")
        elif (pilihan == "2"):
            os.system('cls')
            print("elemen saat ini ",angka)
            pop()
            tampilkan(angka)
            print("-------------------------------")
        elif (pilihan == "3"):
            os.system('cls')
            print("cek isempty")
            isempty()
            print("-------------------------------")
        elif (pilihan == "4"):
            os.system('cls')
            print("elemen saat ini :",angka)
            top()
            print("-------------------------------")
        elif (pilihan == "5"):
            os.system('cls')
            print("elemen saat ini :", angka)
            noel()
            print("-------------------------------")
        elif (pilihan == "6"):
            os.system('cls')
            tampilkan(angka)
            print("-------------------------------")
        else:
            pilih = "enter/ n"

mainmenu()