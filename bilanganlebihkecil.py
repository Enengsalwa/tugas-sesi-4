bila = float(input("masukan bilangan a :"))
bilb = float(input("masukan bilangan b :"))
bilc = float(input("masukan bilangan c :"))

if bila < bilb and bilc:
    print(f"{bila} < {bilb} and {bilc}")
elif bilb < bila and bilc:
    print(f"{bilb} < {bila} and {bilc}")
elif bilc < bila and bilb:
    print(f"{bilc} < {bila} and {bilb}")
    