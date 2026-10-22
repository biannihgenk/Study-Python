#aplikasi struk kasir with python

print("====================================")
print("     APLIKASI STRUK KASIR PYTHON    ")
print("====================================")
input("Tekan Enter untuk memulai...")
kasir = input("Masukkan nama kasir: ")
toko = input("Masukkan nama toko: ")
print("====================================")
print("         STRUK PEMBELIAN BARANG      ")
print("====================================")
print("list barang yang dibeli: ")
barang = {
    "1": {
        "nama": "Susu",
        "harga": 10000
    },
    "2": {
        "nama": "Roti",
        "harga": 5000
    },
    "3": {
        "nama": "Telur",
        "harga": 3000
    }
}
print("1. Susu")
print("2. Roti")
print("3. Telur")
pilihan = input("pilih brang yang dibeli (1/2/3): ")
if pilihan == "1":
    print("Anda membeli Susu harga Rp. 10.000")
elif pilihan == "2":
    print("Anda membeli Roti harga Rp. 5.000")
elif pilihan == "3":
    print("Anda membeli Telur harga Rp. 3.000")
else:
    print("Pilihan tidak valid")

total_barang = int(input("Masukkan jumlah barang: "))
if pilihan == "1":
    print("nama barang: Susu")
    print("jumlah barang:", total_barang)
    print("total harga:", total_barang * 10000)
    total_susu = total_barang * 10000
elif pilihan == "2":
    print("nama barang: Roti")
    print("jumlah barang:", total_barang)
    print("total harga:", total_barang * 5000)
elif pilihan == "3":
    print("nama barang: Telur")
    print("jumlah barang:", total_barang)
    print("total harga:", total_barang * 3000)
total_uang = int(input("Masukkan total uang yang dibayarkan: "))
total_kembalian = total_uang - (total_barang * barang[pilihan]["harga"])

print("====================================")

print("struk pembelian barang")
print("nama kasir:", kasir)
print("nama toko:", toko)
print("barang yang dibeli:", barang[pilihan]["nama"])
print("jumlah barang:", total_barang)
if pilihan == "1":
    print("total harga:", total_barang * 10000)
elif pilihan == "2":
    print("total harga:", total_barang * 5000)
elif pilihan == "3":
    print("total harga:", total_barang * 3000)
print("total uang yang dibayarkan:", total_uang)
print("total kembalian:", total_kembalian)

print("Terima kasih telah berbelanja di", toko)
print("====================================")