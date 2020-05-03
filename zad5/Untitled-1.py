a = int(input("Podaj 1 liczbe: "))
b = int(input("Podaj 2 liczbe: "))
c = int(input("Podaj 3 liczbe: "))

if (a > 0 and a <= 10 and a > b) or (a > 0 and a <= 10 and b > c) :
    print("Warunek spelniony")
else:
     print ("Warunek nie zostal spelniony")