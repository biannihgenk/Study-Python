#belajar operasi matematika

ganteng = True
jelek = True
hasil = ganteng or jelek #OR
print("Bian Ganteng atau jelek:", hasil)
hasil2 = ganteng and jelek #AND
print("Bian Ganteng dan jelek:", hasil2)
hasil3 = not ganteng #NOT
print("Bian Tidak Ganteng:", hasil3)
hasil4 = ganteng and not jelek #NAND
print("Bian Ganteng dan Tidak jelek:", hasil4)
hasil5 = ganteng or not jelek #XOR
print("Bian Ganteng atau Tidak jelek:", hasil5)

#XOR
hasil6 = ganteng ^ jelek
print("Bian Ganteng atau jelek:", hasil6)

#macam-macam simbol operasi matematika

#operasi logika and
print(" ----Operasi logika AND----")
a = True
b = True
c = a and b
print("True and True:", c)

a = True
b = False
c = a and b
print("True and False:", c)

a = False
b = True
c = a and b
print("False and True:", c)

a = False
b = False
c = a and b
print("False and False:", c)


#operasi logika or
print(" ----Operasi logika OR----")
a = True
b = True
c = a or b
print("True or True:", c)

a = True
b = False
c = a or b
print("True or False:", c)

a = False
b = True
c = a or b
print("False or True:", c)

a = False
b = False
c = a or b
print("False or False:", c)

#operasi logika not
print(" ----Operasi logika NOT----")
a = True
b = not a
print("Not True:", b)

a = False
b = not a
print("Not False:", b)

a = True
b = False
c = a and b
print("True and False:", c)

#operasi logika xor
print(" ----Operasi logika XOR----")
a = True
b = True
c = a ^ b
print("True XOR True:", c)

a = True
b = False
c = a ^ b
print("True XOR False:", c)

a = False
b = True
c = a ^ b
print("False XOR True:", c)

a = False
b = False
c = a ^ b
print("False XOR False:", c)

#operasi logika NAND
print(" ----Operasi logika NAND----")
a = True
b = True
c = not (a and b)
print("True NAND True:", c)

a = True
b = False
c = not (a and b)
print("True NAND False:", c)

a = False
b = True
c = not (a and b)
print("False NAND True:", c)

a = False
b = False
c = not (a and b)
print("False NAND False:", c)



#operasi bitwise
print(" ----Operasi Bitwise----")

print(" ----Operasi Bitwise OR ----")
a = 9
b = 5
c = a | b
print("a =", a, "in binary:", format(a, '08b'))
print("b =", b, "in binary:", format(b, '08b'))
print("a | b =", c, "in binary:", format(c, '08b'))

print(" ----Operasi Bitwise AND ----")
c = a & b
print("a =", a, "in binary:", format(a, '08b'))
print("b =", b, "in binary:", format(b, '08b'))
print("a & b =", c, "in binary:", format(c, '08b'))

print(" ----Operasi Bitwise XOR ----")
c = a ^ b
print("a =", a, "in binary:", format(a, '08b'))
print("b =", b, "in binary:", format(b, '08b'))
print("a ^ b =", c, "in binary:", format(c, '08b'))


print(" ----Operasi Assignment ----") #perhitungan berurutan sesuai dengan intruksi yang diberikan
a = 10
print("Nilai awal a:", a)
a += 5
print("Nilai a setelah a += 5:", a)
a -= 3
print("Nilai a setelah a -= 3:", a)
a *= 2
print("Nilai a setelah a *= 2:", a)
a /= 4
print("Nilai a setelah a /= 4:", a)