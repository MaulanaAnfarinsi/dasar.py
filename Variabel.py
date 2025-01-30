Nama = "Lana"
print(Nama)
print(type(Nama))

#LIST#
contoh_list = [10, 2, 20.0, "Lana"]
print(contoh_list[2])

contoh_list.append("Maulana")
print(contoh_list)

#TUPLE#
contoh_tuple =(10, 2, 30)
print(contoh_tuple)

#SET#
contoh_set = {10, 20, 30}
print(contoh_set)

contoh_set.add(23)
print(contoh_set)

#DICTIONARY#
contoh_dictionary = {
    "nama": "Maulana",
    "umur": 20
}
print(contoh_dictionary["nama"])
print(contoh_dictionary["umur"])

#OPERATOR#
import numpy as np

np_array = np.array([1, 2, 3, 4])
print(np_array + 2)  

np_math = np.array([9, 5, 6, 7])
print(np_math * 3) #output [27 15 18 21]


np_array = np.array([10, 20, 30, 40])
print(np_array ** 2)  

# Membuat array NumPy
np_perkalian = np.array([20, 23, 26, 27, 50])

# Mengalikan array dengan 3 dan mencetak hasilnya
print(np_perkalian * 3)

#Percabangan
Angka = 44

if Angka < 40:
    print("Angka Lebih kecil dari 40")
elif Angka > 40:
    print("Angka lebih besar dari 40")
else:
    print("Angka lebih besar atau sama dengan 40")

#Perulangan break
for x in range(3): 
    if x == 1:             
        break              
    print("x=" + str(x))
    if x == 1:
        break 

#Perulangan Continue
for x in range(3, 0, -1):
    if x % 2 == 0:
        continue
    print(x)

#Exception
angka = 10
try:
    print(angka/2)
except:
    print("Proses panggilan tidak di temukan")
