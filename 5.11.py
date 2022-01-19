we = open("we11.txt", "r", encoding="utf-8")
wy = open("wy11.txt", "w", encoding="utf-8")

def wypisz_macierz(m):
    for w in m:
        for v in w:
            print(v if v else ' ', end=' ')
        print()
    print()

def wypisz_macierz_do_pliku(m):
    for w in m:
        for v in w:
            wy.write(str(v) if v else ' ')
            wy.write(' ')
        wy.write('\n')
    wy.write('\n')

def transponuj(m):
    m_trans = list(zip(*m))
    m_trans = [list(sublist) for sublist in m_trans]
    return m_trans


macierz = []
macierz_a = []
macierz_b = []
macierz_c = []

# wczytujemy wartości z pliku do macierzy
for linia in we:
    macierz.append([])
    for v in linia.split():
        v = int(v)
        macierz[-1].append(v)

# kopie macierzy dla osobnych przykładów
for wiersz in macierz:
    macierz_a.append(wiersz.copy())
    macierz_b.append(wiersz.copy())
    macierz_c.append(wiersz.copy())


print("Macierz wczytana z pliku:")
wypisz_macierz(macierz)

# wyliczenie minimalniej i maksymalnej długości wiersza w macierzy
min_wiersz = min(map(len, macierz))
max_wiersz = max(map(len, macierz))

# skracanie macierzy a
for i in range(len(macierz_a)):
    macierz_a[i] = macierz_a[i][0:min_wiersz]

# wydłużenie macierzy b
for i in range(len(macierz_b)):
    dlugosc_wiersza = len(macierz_b[i])
    for j in range(max_wiersz - dlugosc_wiersza):
        macierz_b[i].append(macierz_b[i][-1])

# wypełnienie macierzy c niczym żeby później nie było problemów z transpozycją
for i in range(len(macierz_c)):
    dlugosc_wiersza = len(macierz_c[i])
    for j in range(max_wiersz - dlugosc_wiersza):
        macierz_c[i].append(None)

print("Macierz przycięta:")
wypisz_macierz(macierz_a)

print("Macierz wydłużona:")
wypisz_macierz(macierz_b)

print("Macierz c (czyli w sumie nic się nie zmieniło):")
wypisz_macierz(macierz_c)

print("Transponowana macierz przycięta:")
wypisz_macierz(transponuj(macierz_a))

print("Transponowana macierz wydłużona:")
wypisz_macierz(transponuj(macierz_b))

print("Transponowana macierz c:")
wypisz_macierz(transponuj(macierz_c))

wypisz_macierz_do_pliku(transponuj(macierz_a))
wypisz_macierz_do_pliku(transponuj(macierz_b))
wypisz_macierz_do_pliku(transponuj(macierz_c))

we.close()
wy.close()