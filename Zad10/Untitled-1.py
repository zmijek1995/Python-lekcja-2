# for x in range (0, 1001, 5):
#     print(str(x) + " ")
x = int(input("Podaj wysokosc wiezy: "))
if x > 0 and x <= 10:
    for i in range(1, x+1):
        print(i * "A")
else:
    print("Zla wysokosc wiezy!!!")