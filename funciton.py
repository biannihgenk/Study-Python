#belajar function python

def halo():
    print("Halo, selamat datang di function python")

print("Sebelum memanggil function")
halo() #ini cara kita manggilnya

#funciton dengan parameter/argument
def halo(nama):
    print("Halo", nama, "selamat datang di function python")

def say_hello(list_nama):
    data_kelas = list_nama.copy() #mengcopy data list agar tidak mengubah data asli
    for nama in data_kelas:
        print("Halo", nama, "selamat datang di function python")


data_kelas = ["Andi", "Budi", "Caca", "Deni", "Eka"]

say_hello(data_kelas) #ini cara kita manggilnya
   