#episode While Loop,continue,break

#Break adalah langsung finish
#Continue adalah lanjut ke step selanjutnya (melewati step itu)

    # while loop

# while kondisi:
# 	aksi ini
# 	aksi itu

# akhir dari program

angka = 0
print(f"Angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka selanjutnya -> {angka}")

    if angka == 2:
        print("nicee")
        break

    print("aku ganteng")

print("cukupp")



# Break
# angka = 0

# while angka < 5:
# 	angka += 1
# 	print(f"angka sekarang = {angka}")

# 	if angka == 3:
# 		print("nice!")
# 		break

# 	print("wassup!")

# print("cukuuup finish!")

# data_int = int(input("hitung sampai = "))

# angka = 0

# while True:
# 	angka += 1
# 	print(f"count = {angka}")

# 	if angka == data_int:
# 		print("nice!")
# 		break

# 	print("wassup!")

# print("cukuuup finish!")

# angka = 0
# print(f"Angka sekarang -> {angka}")

# while angka < 5:
#     angka += 1
#     print(f"angka selanjutnya -> {angka}")
	
# if angka == 2:
#     print("nicee")
#     continue

#     print("aku ganteng")

# print("cukupp")

# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi


angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
	angka += 1
	print(f"angka sekarang -> {angka}") # aksi 1

	if angka == 3:
		print("nice!")
		continue # akan membuat loop meloncat ke step selanjutnya

	print("whassup!") # aksi 2

print("Pinish!")