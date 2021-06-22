import os
queue =[]

def push (value) :
    queue.append(value)

def deuque () :
    print("elemen yang dihapus :", queue.pop(0))

def noel () :
    #print (len (queue))
    print("jumlah elemen  :", len(queue))
def top () :
    top = len (queue) - 1
    if top  < 0:
        print("ora enng")
    else :
        print ("elemen terakhir :",queue[top])

def isempty () :
    if len (queue) == 0:
        print ("True")
    else:
        print ("false")

def tampilkan () :
    print ("semua elemen queue :",queue)



def mainmenu():
    print("=========================")
    print("|         QUEUE         |")
    print("=========================")
    print("1. ENQUEUE ")
    print("2. DEQUEUE ")
    print("3. cek Empty")
    print("4. Tampilkan elemen terakhir")
    print("5. jumlah elemen dari QUEUE")
    print("6. tampilkan semua QUEUE ")
    print("-------------------------")
    pilih = "y"
    while (pilih == "y"):
        pilihan = str(input(("Silakan masukan pilihan anda [1/2/3/4/5/6] : ")))
        if (pilihan == "1"):
            os.system('cls')
            push(int(input("masukkan elemen : ")))
            print("elemen saat ini :",queue)
            print("---------------------------------")
        elif (pilihan == "2"):
            os.system('cls')
            print("elemen saat ini :",queue)
            deuque()
            print("elemen setelah dihapus ",)
            tampilkan()
            print("---------------------------------")
        elif (pilihan == "3"):
            os.system('cls')
            print("cek isempty")
            isempty()
            print("---------------------------------")
        elif (pilihan == "4"):
            os.system('cls')
            print("elemen saat ini :",queue)
            top()
            print("---------------------------------")

        elif (pilihan == "5"):
            os.system('cls')
            print("elemen saat ini :", queue)
            noel()
            print("---------------------------------")

        elif(pilihan == "6"):
            os.system('cls')
            tampilkan()
            print("---------------------------------")

        else:
            pilih = "enter/n"

mainmenu()
