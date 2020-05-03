lista = []
while True:
    x = int(input("Podaj liczbe do listy: "))
    lista.append(x)
    
    print("Czy dodac kolejna liczbe? t/n: ")
    z = str(input())
    if z[0] == 'n':  break
print(lista)