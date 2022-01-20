plik = open("we21.txt", "r", encoding="utf-8")

for linia in plik:
    liczba, okres = tuple(linia.strip().split('('))
    okres = okres[0:-1]
    część_całkowita, ułamek = tuple(liczba.split(','))
    mnożnik_x = 10 ** len(ułamek)
    mnożnik_y = 10 ** len(ułamek + okres)
    x = część_całkowita + ułamek
    y = część_całkowita + ułamek + okres
    licznik = int(y) - int(x)
    mianownik = int(mnożnik_y) - int(mnożnik_x)
    print(f'{część_całkowita},{ułamek}({okres}) -> {licznik}/{mianownik}')



