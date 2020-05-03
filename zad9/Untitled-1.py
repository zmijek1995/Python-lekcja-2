x = int(input("Podaj liczbe: "))
def suma(a):
    s= 0
    while a > 0:
        s = s + a % 10
        a = a // 10       
    return s
print(suma(x))