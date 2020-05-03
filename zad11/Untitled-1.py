w = int(input('Podaj wysokosc: '))
if 3 <= w <= 9:
    for x in range(1, w+1):
        if x % 2:
            print((x * 'O').center(w, ' '))
    for x in reversed(range(1, w+1)):
        if x % 2 and x is not w:
            print((x * 'O').center(w, ' '))