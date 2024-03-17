pilihan = ["batu", "gunting", "kertas"]

tim1 = input("tim 1 lakukan pilihanmu :")
tim2 = input("tim 2 lakukan pilihanmu :")

if tim1 == tim2 :
    print("ini seri")
elif tim1 == "batu" and tim2 == "gunting":
    print("tim1 menang")
elif tim1 == "kertas" and tim2 == "batu":
    print("tim 1 menang")
elif tim1 == "gunting" and tim2 == "kertas":
    print("tim 1 menang")
else:
    print("tim 2 menang")