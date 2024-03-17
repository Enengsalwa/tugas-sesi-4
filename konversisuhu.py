celcius = float(input("masukan nilai celcius :"))
fahrenheit = float(input("masukan nilai fahrenheit :"))

celcius = (fahrenheit -32) * 5/9
fahrenheit = (celcius * 9/5) + 32
pilihan_konversi = input ("masukan pilihan :")
print ("pilihan konversi :")
print ("1. celcius ke fahrenheit :", fahrenheit)
print ("2. fahrenheit ke celcius :", celcius)

if pilihan_konversi == '1' :
    print ("suhu dalam fahrenheit ", fahrenheit)
elif pilihan_konversi == '2':
    print ("suhu dalam celcius ", celcius)
else:
    print ("pilihan tidak valid, silakan pilih 1 atau 2")
    