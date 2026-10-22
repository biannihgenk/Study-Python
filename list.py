# #episode List :       

# ## --- LIST ---

# # Kumpulan data numbers
# data_angka = [1,5,2,3]
# print(data_angka)

# # Kumpulan data string
# data_string = ["ucup","otong","odah"]
# print(data_string)

# # Kumpulan data boolean
# data_boolean = [True, False, True, True]
# print(data_boolean)

# # Kumpulan campuran
# data_campuran = [1,"bala-bala",2,"cireng","ucup",True,"otong",False]
# print(data_campuran)

# ## cara alternatif membuat list
# data_range = range(0,10,2) # range(start,stop,step)
# print(data_range)
# data_list = list(data_range)
# print(data_list)

# # membuat list dengan for loop, list comprehension
# list_pakai_for = [i for i in range(0,10)]
# print(list_pakai_for)

# # membuat list pake for pake if
# list_pake_for_if = [i for i in range(0,10) if i != 5]
# print(list_pake_for_if)

# list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
# print(list_pake_for_if)

# list_pake_for_if = [i**2 for i in range(0,10) if i%2 !=0]
# print(list_pake_for_if)

#operasi List

#index    0       1      2
data = ["Bian","Alul","Nizam"]
#ambil data
data1 = data[0]
print(data1)

#mengambil info panjang data
panjang_data = len(data)
print(panjang_data)

#Manipulasi data list

#menambahkan data list
data.insert(1,"rehan")
print(data)

#menambahkan di akhir
data.append("joni")
print(data)

#gabungin list
data_baru = ["keren","elek","biasa"]
data.extend(data_baru)
print(data)

#merubah data
data[1] = "nizam"
print(data)

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")

#operasi data

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

jumlah_4 = data_angka.count(4)
print(jumlah_4)

#menurutkan list
data_angka.sort()
print(data_angka)
data_angka.reverse()
print(data_angka)

#teknik menduplikat data
a = ["bian","nizar","ganteng"]

b = a #"""duplikat by reference ,namun ini itu memiliki almaat data yang sama ,alhasil apabila kita menganti salah satu,maka akan terkena semua""""""
print(b)

c = a.copy() #duplikat dengan copy ,memiliki alamat yang berbeda
print(c)

#nested list

data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,6,7]

print(f"list 2D = {list_2D}")

# contoh penggunaan

peserta_0 = ["ucup",25,"Laki-laki"]
peserta_1 = ["otong",10,"Laki-laki"]
peserta_2 = ["dedeh",50,"Wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
	print(f"nama\t: {peserta[0]}")
	print(f"umur\t: {peserta[1]}")
	print(f"gender\t: {peserta[2]}\n")


# coppy biasa dengan reference

list_copy = list_peserta.copy();
print(f"peserta = {list_copy}")
peserta_0[0] = "michael"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")
#copy nya dengan addres yang sama ,sehingga kalau ganti 1 maka ganti semua

# Solusinya kita gunakan deepcopy

from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy =  deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data deep = {data_2D_deepcopy}")
