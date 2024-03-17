bila = float(input("masukan bilangan a :"))
bilb = float(input("masukan bilangan b :"))
bilc = float(input("masukan bilangan c :"))

if bila > bilb and bilc:
    print(f"{bila} > {bilb} and {bilc}")
elif bilb > bila and bilc:
    print(f"{bilb} > {bila} and {bilc}")
elif bilc > bila and bilb:
    print(f"{bilc} > {bila} and {bilb}")
elif bila == bilb and bila > bilc and bilb > bilc:
    print(f"{bila} and {bilb} sama besar dan lebih besar dari {bilc}")
elif bila == bilc and bila > bilb and bilc > bilb:
    print(f"{bila} and {bilc} sama besar dan lebih besar dari {bilb}")
elif bilb == bilc and bilb > bila and bilc > bila:
    print(f"{bilb} and {bilc} sama besar dan lebih besar dari {bilb}")
    
else:
    print(f"{bila}, {bilb} and {bilc} sama besar")
    