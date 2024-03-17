import math
a = float(input("masukan angka untuk sisi a :"))
b = float(input("masukan angka untuk sisi b :"))
c = float(input("masukan angka untuk sisi c :"))

s = (a+b+c)/2
L = math.sqrt(s*(s-a)*(s-b)*(s-c))
K = a+b+c

print ("Luas segitiga adalah",L)
print ("keliling segitiga adalah",K)