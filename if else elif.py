# #episode If ELSE ELIF
# # if condition: aksi
# # else: aksi
# # elif condition: aksi

# orang_ganteng = input("Siapa orang ganteng itu? ")

# if orang_ganteng == "bian":
#     print("ya benar orang ganteng itu bian")
# elif orang_ganteng == "joko":
#     print("joko juga ganteng")
# else:
#     print("bukan orang ganteng itu bian")


# print("selesai \n")

# print("*"*100)
# print("Selamat datang di program kalkulator sederhana")
# print("*"*100)

# input1 = int(input("Masukkan angka pertama: ")) 
# operator = input("Masukkan operator (+, -, *, /): ")
# input2 = int(input("Masukkan angka kedua: "))

# if operator == "+":
#     hasil = input1 + input2
#     print("Hasil penjumlahan:", hasil)
# elif operator == "-":
#     hasil = input1 - input2
#     print("Hasil pengurangan:", hasil)
# elif operator == "*":
#     hasil = input1 * input2
#     print("Hasil perkalian:", hasil)
# elif operator == "/":
#     if input2 != 0: #maksudnya adalah jika input2 tidak sama dengan 0 maka akan melakukan pembagian, jika sama dengan 0 maka akan men
#         hasil = input1 / input2
#         print("Hasil pembagian:", hasil)
#     else:
#         print("Error: Pembagian dengan nol tidak diperbolehkan.")

# else:
#     print("Operator tidak valid. Silakan gunakan +, -, *, atau /.")

# print("Terima kasih telah menggunakan kalkulator sederhana ini.")


# print("selesai \n")

print("*"*100)
print("Selamat datang di program penentuan nilai")
print("*"*100)

nilai = int(input("Masukkan nilai Anda (0-100): "))

if nilai == 100:
    print("kamu sangat jenius")
elif nilai > 90:
    print("kamu lumayan pintar")
elif nilai > 80:
    print("kamu cukup pintar")