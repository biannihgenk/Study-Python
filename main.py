#TIPE DATA DALAM PYTHON
#1. Tipe Data Angka (INTEGER, FLOAT, COMPLEX)
a = 10 #INTEGER
b = 3.14 #FLOAT
c = 2+3j #COMPLEX

# Tipe Data String
c = "Hello, World!" #STRING
print("Tipe Data String:", c ,"type:", type(c))

# Tipe Data Boolean
d = True #BOOLEAN
print("Tipe Data Boolean:", d ,"type:", type(d))

# Tipe Data List
e = [1, 2, 3, 4, 5] #LIST
print("Tipe Data List:", e ,"type:", type(e))


#mengkonversi tipe data
#1. Konversi ke Integer
f = int(2.5)
print("Konversi ke Integer:", f ,"type:", type(f))

a = int("10") #int("10") akan mengkonversi string "10" menjadi integer 10
print("Konversi ke Integer:", a ,"type:", type(a))

b = bool(1) #bool(1) akan mengkonversi integer 1 menjadi boolean True
print("Konversi ke Boolean:", b ,"type:", type(b))

#2. Konversi ke Float
g = float(10) #float(10) akan mengkonversi integer 10 menjadi float 10.0
print("Konversi ke Float:", g ,"type:", type(g))


#Episode Input dari user
nama = input("Masukkan nama Anda:") #input() akan meminta input dari user dan menyimpannya dalam variabel nama
print("Nama Anda adalah:", nama)

birth_year = int(input("Masukkan tahun lahir Anda:")) #input menggunakan integer
age = 2026 - birth_year #menghitung umur    
print("Umur Anda adalah:", age)

print("----EPISOD BELAJAR NGODING OPERASI MTK DASAR----")

angka1 = int(input("input nomor anda : ")) #kalau operasi matematika harus ada intnya karena input() akan mengembalikan tipe data string, sehingga harus dikonversi ke integer agar bisa dilakukan operasi matematika
angka2 = int(input("input nomor anda yang kedua :"))
print("hasil penjumlahan dari", angka1, "+", angka2, "=", angka1 + angka2)  #kenapa kok harus ada intnya

print("hasil pengurangan dari", angka1, "-", angka2, "=", angka1 - angka2)

print("hasil perkalian dari", angka1, "*", angka2, "=", angka1 * angka2)

print("hasil pembagian dari", angka1, "/", angka2, "=", angka1 / angka2)

print("hasil modulus dari", angka1, "%", angka2, "=", angka1 % angka2) #modulus adalah sisa hasil bagi

print("hasil pangkat dari", angka1, "**", angka2, "=", angka1 ** angka2) #pangkat adalah hasil perkalian berulang

print("hasil pembagian bulat dari", angka1, "//", angka2, "=", angka1 // angka2) #pembagian bulat adalah hasil pembagian tanpa sisa

print("----EPISOD BELAJAR NGODING KALKULATOR----")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

print("Pilih operasi matematika:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == "1":
    hasil = a + b
    print("Hasil penjumlahan:", hasil)
elif pilihan == "2":
    hasil = a - b
    print("Hasil pengurangan:", hasil)
elif pilihan == "3":
    hasil = a * b
    print("Hasil perkalian:", hasil)
elif pilihan == "4":
    hasil = a / b
    print("Hasil pembagian:", hasil)
else:
    print("Pilihan tidak valid")

print("Terima kasih telah menggunakan kalkulator sederhana ini.")
print("Pilih lagi untuk melakukan operasi matematika lainnya atau keluar dari program.")
print("1. Ya")
print("2. Tidak")
pilihan_lagi = input("Masukkan pilihan (1/2): ")
if pilihan_lagi == "1":
    # Memanggil kembali kalkulator
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))

    print("Pilih operasi matematika:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        hasil = a + b
        print("Hasil penjumlahan:", hasil)
    elif pilihan == "2":
        hasil = a - b
        print("Hasil pengurangan:", hasil)
    elif pilihan == "3":
        hasil = a * b
        print("Hasil perkalian:", hasil)
    elif pilihan == "4":
        hasil = a / b
        print("Hasil pembagian:", hasil)
    else:
        print("Pilihan tidak valid")

else:
    print("Terima kasih telah menggunakan kalkulator sederhana ini.")

print("program to do list")

print()