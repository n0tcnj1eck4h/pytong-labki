pliczek = open("we3.txt", "r", encoding="utf-8")
linijeczki = pliczek.readlines()

lista_cyferek = []


for linijeczka in linijeczki:
    cyferka = int(linijeczka)
    lista_cyferek.append(cyferka)

# super, mamy listę cyferek
print(lista_cyferek)

lista_do_podpunktu_e = lista_cyferek.copy()
lista_do_podpunktu_e.reverse()

# a)
suma_elementów_listy = sum(lista_cyferek)

"""
 b)
wyznaczyć największą liczbę ujemną i najmniejszą dodat-
nią, oraz największą dodatnią i najmniejszą ujemną; zero
nie jest ani dodatnie, ani ujemne.
"""

największa_liczba_ujemna =    max(filter(lambda x: x < 0, lista_cyferek))
najmniejsza_liczba_dodatnia = min(filter(lambda x: x > 0, lista_cyferek))
najmniejsza_liczba_ujemna =   min(filter(lambda x: x < 0, lista_cyferek))
największa_liczba_dodatnia =  max(filter(lambda x: x > 0, lista_cyferek))
print(największa_liczba_ujemna)
print(najmniejsza_liczba_dodatnia)
print(najmniejsza_liczba_ujemna)
print(największa_liczba_dodatnia)

# c) posortować te liczby
# malejąco co do wartości

lista_cyferek.sort()
print("Cyferki rosnąco:", lista_cyferek)

lista_cyferek.sort(key=lambda x: len(str(x)))
print("Cyferki rosnąco po ilości znaków:", lista_cyferek)

print("lista_do_podpunktu_e: ", lista_do_podpunktu_e)