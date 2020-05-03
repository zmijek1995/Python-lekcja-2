while True:
    x = int(input("Podaj liczbe do potegowania: "))
    print("Kwadrat wynosi: " + str(x ** 2))
    print("Czy powtórzyć jeszcze raz? t/n: ")
    z = str(input())
    if z[0] == 'n': break