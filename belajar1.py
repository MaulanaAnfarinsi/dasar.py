def hitung_kecepatan():
    print("hitung kecepatan ready!")
    jarak =float(input("masukan jarak: "))
    waktu =float(input("masukan waktu: "))
    kecepatan = jarak * waktu
    print("kecepatan: ", kecepatan, "\n")


def luas_segitiga():
     print("hitung segitiga ")
     alas  =float(input("masukan alas: "))
     tinggi =float(input("masukan tinggi: "))
     luas = 0.5 * (alas * tinggi)
     print("luas segitiga adalah: ", luas, "\n")

def luas_balok():
     print("hitung luas balok ")
     panjang=float(input("masukan panjang: "))
     lebar=float(input("masukan alas: "))
     tinggi =float(input("masukan tinggi: "))
     luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
     print("luas balok adalah: ", luas, "\n")

def luas_bola():
     print("hitung luas bola ")
     r =float(input("masukan jari - jari: "))
     luas = 4 * 3.14 * (r**2)
     print("luas bola adalah: ", luas, "\n")

while True:
    UserInput = int(input("pilih rumus yang akan dipakai: \n\n1.hitung kecepatan\n2.luas segitiga\n3.luas_balok\n4.luas_bola\n\n0.keluar program\n\npilih nomor berapa: "))
    if(UserInput == 1):
        hitung_kecepatan()
    elif(UserInput ==2):
        luas_segitiga()
    elif(UserInput ==3):
        luas_balok()
    elif(UserInput ==4):
        luas_bola()
    else:
        break
