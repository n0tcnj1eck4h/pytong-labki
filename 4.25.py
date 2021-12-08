slownik = {
    0: 'zero',
    1: 'jeden',
    2: 'dwa',
    3: 'trzy',
    4: 'cztery',
    5: 'pięć',
    6: 'sześć',
    7: 'siedem',
    8: 'osiem',
    9: 'dziewięć',
    10: 'dziesięć',
    11: 'jedenaście',
    12: 'dwanaście',
    13: 'trzynaście',
    14: 'czternaście',
    15: 'piętnaście',
    16: 'szesnaście',
    17: 'siedemnaście',
    18: 'osiemnaście',
    19: 'dziewiętnaście',
    20: 'dwadzieścia',
    30: 'trzydzieści',
    40: 'czterdzieści',
    50: 'piędziesiąt',
    60: 'sześćdziesiąt',
    70: 'siedemdziesiąt',
    80: 'osiemdziesiąt',
    90: 'dziewięćdziesiąt',
    100: 'sto',
    200: 'dwieście',
    300: 'trzysta',
    400: 'czterysta',
    500: 'pięćset',
    600: 'sześćset',
    700: 'siedemset',
    800: 'osiemset',
    900: 'dziewiętset'
}

odmiana = {
    0: 'tysięcy',
    1: 'tysiąc',
    2: 'tysiące',
    3: 'tysiące',
    4: 'tysiące',
    5: 'tysięcy',
    6: 'tysięcy',
    7: 'tysięcy',
    8: 'tysięcy',
    9: 'tysięcy',
}

#n = int(input("PODAJ N: "))
A = {}


def przetlumacz(n):
    if n <= 20:
        return slownik.get(n)

    if n < 100:
        dziesitki = ((n % 100) // 10) * 10
        reszta = n % 10
        return slownik.get(dziesitki) + ' ' + przetlumacz(reszta)

    if n < 1000:
        setki = ((n % 1000) // 100) * 100
        reszta = n % 100
        if reszta != 0:
            return slownik.get(setki) + ' ' + przetlumacz(reszta)
        else:
            return slownik.get(setki)

    if n < 10000:
        tysiące = n // 1000
        reszta = n % 1000
        if reszta != 0:
            return slownik.get(tysiące) + ' ' + odmiana.get(tysiące) + ' ' + przetlumacz(reszta)
        else:
            return slownik.get(tysiące) + ' ' + odmiana.get(tysiące)

for i in range(10000):
    dsfkjbsdfjhk = przetlumacz(i)
    A[i] = dsfkjbsdfjhk

print(A)



