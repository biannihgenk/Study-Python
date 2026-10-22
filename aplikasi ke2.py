# ============================================================
# WIDTH / MENGATUR LEBAR STRING
# ============================================================

# Width digunakan untuk mengatur lebar minimal
# dari sebuah data ketika ditampilkan.

# Bentuk dasar:
#
# f"{data:>10}"
#
# 10 = lebar minimal
# >  = rata kanan


# ============================================================
# 1. WIDTH DASAR
# ============================================================

nama = "Ucup"

print(f"|{nama:>10}|")

# Hasil:
# |      Ucup|
#
# "Ucup" memiliki 4 karakter.
# Width = 10.
# Maka Python menambahkan 6 spasi di sebelah kiri.


# ============================================================
# 2. WIDTH BUKAN BATAS MAKSIMAL
# ============================================================

nama = "Ucup Surucup"

print(f"|{nama:>5}|")

# Hasil:
# |Ucup Surucup|
#
# Walaupun width = 5,
# teks tetap ditampilkan seluruhnya.
#
# Jadi width adalah:
# MINIMAL lebar, bukan maksimal.


# ============================================================
# 3. ALIGNMENT
# ============================================================

# Alignment digunakan untuk menentukan posisi data
# di dalam width.


# < = RATA KIRI
nama = "Ucup"

print(f"|{nama:<10}|")

# Hasil:
# |Ucup      |


# > = RATA KANAN
print(f"|{nama:>10}|")

# Hasil:
# |      Ucup|


# ^ = RATA TENGAH
print(f"|{nama:^10}|")

# Hasil:
# |   Ucup   |


# Jadi:
#
# <  = kiri
# >  = kanan
# ^  = tengah


# ============================================================
# 4. WIDTH PADA ANGKA
# ============================================================

umur = 17
tinggi = 150.1
nomor_sepatu = 44

print(f"|{umur:>10}|")
print(f"|{tinggi:>10}|")
print(f"|{nomor_sepatu:>10}|")

# Width dapat digunakan pada:
# - String
# - Integer
# - Float
# dan tipe data lainnya yang mendukung formatting.


# ============================================================
# 5. MEMBUAT TABEL SEDERHANA
# ============================================================

nama1 = "Ucup"
nama2 = "Budi"
nama3 = "Andi"

umur1 = 17
umur2 = 16
umur3 = 15

print(f"{'Nama':<15}{'Umur':>5}")
print("-" * 20)

print(f"{nama1:<15}{umur1:>5}")
print(f"{nama2:<15}{umur2:>5}")
print(f"{nama3:<15}{umur3:>5}")

# Penjelasan:
#
# {'Nama':<15}
# -> "Nama" memiliki width 15 dan rata kiri.
#
# {umur1:>5}
# -> umur memiliki width 5 dan rata kanan.
#
# Width berguna untuk membuat tampilan tabel
# agar lebih rapi.


# ============================================================
# 6. KARAKTER PENGISI
# ============================================================

# Secara default, ruang kosong diisi dengan spasi.
#
# Kita bisa mengganti spasi dengan karakter lain.


nama = "Ucup"

print(f"{nama:*^10}")

# Hasil:
# ***Ucup***
#
# * = karakter pengisi
# ^ = rata tengah
# 10 = width


# ============================================================
# 7. KARAKTER PENGISI + RATA KANAN
# ============================================================

print(f"{nama:*>10}")

# Hasil:
# ******Ucup
#
# * = karakter pengisi
# > = rata kanan
# 10 = width


# ============================================================
# 8. KARAKTER PENGISI + RATA KIRI
# ============================================================

print(f"{nama:*<10}")

# Hasil:
# Ucup******
#
# * = karakter pengisi
# < = rata kiri
# 10 = width


# ============================================================
# 9. FORMAT WIDTH LENGKAP
# ============================================================

# Bentuk umum:
#
# {data:fill alignment width}
#
# Contoh:
#
# f"{nama:*^10}"
#
# *  = fill / karakter pengisi
# ^  = alignment / posisi
# 10 = width / lebar


# ============================================================
# 10. CONTOH DATA DIRI
# ============================================================

nama = "Ucup Surucup"
umur = 17
tinggi = 150.1
nomor_sepatu = 44

data_string = f"""
========================================
              DATA DIRI
========================================
Nama          = {nama}
Umur          = {umur}
Tinggi        = {tinggi}
Nomor Sepatu  = {nomor_sepatu}
========================================
"""

print(data_string)


# ============================================================
# 11. DATA DIRI DENGAN WIDTH
# ============================================================

data_string = f"""
========================================
              DATA DIRI
========================================
{"Nama":<15} = {nama}
{"Umur":<15} = {umur}
{"Tinggi":<15} = {tinggi}
{"Sepatu":<15} = {nomor_sepatu}
========================================
"""

print(data_string)


# ============================================================
# RANGKUMAN WIDTH
# ============================================================

# WIDTH
# -> Mengatur lebar minimal sebuah data.


# RATA KIRI
# <

print(f"{'Ucup':<10}")


# RATA KANAN
# >

print(f"{'Ucup':>10}")


# RATA TENGAH
# ^

print(f"{'Ucup':^10}")


# KARAKTER PENGISI
# *

print(f"{'Ucup':*^10}")


# ============================================================
# CHEAT SHEET
# ============================================================

# f"{data:<10}"
# -> width 10, rata kiri


# f"{data:>10}"
# -> width 10, rata kanan


# f"{data:^10}"
# -> width 10, rata tengah


# f"{data:*<10}"
# -> width 10, rata kiri, menggunakan *


# f"{data:*>10}"
# -> width 10, rata kanan, menggunakan *


# f"{data:*^10}"
# -> width 10, rata tengah, menggunakan *


# ============================================================
# INTI YANG HARUS DIINGAT
# ============================================================

# <  = LEFT  / kiri
# >  = RIGHT / kanan
# ^  = CENTER / tengah
#
# angka = WIDTH / lebar minimal
#
# karakter sebelum < > ^
# = karakter pengisi
#
# Contoh:
#
# f"{nama:*^10}"
#
# Artinya:
# nama -> data yang ditampilkan
# *    -> karakter pengisi
# ^    -> rata tengah
# 10   -> lebar minimal 10 karakter
#
# ============================================================
# SELESAI
# ============================================================