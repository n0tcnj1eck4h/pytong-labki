plik = open("we4.txt", "r", encoding="utf-8")

# nieistotne
#def czy_nawiasy_się_zgadzają_w_tym_ciągu_znaków(ciąg_znaków: str):
#    ilość_nawiasów_otwierających = len(list(filter(lambda x: x == '(', list(ciąg_znaków))))
#    ilość_nawiasów_zamykających  = len(list(filter(lambda x: x == ')', list(ciąg_znaków))))
#    return ilość_nawiasów_otwierających == ilość_nawiasów_zamykających

def czy_nawiasy_się_zgadzają_w_tym_ciągu_znaków(ciąg_znaków: str):
    x = 0
    for znak in ciąg_znaków:
        if znak == '(':
            x += 1
        elif znak == ')':
            x -= 1
        if x < 0:
            return False
    return x == 0

for linia in plik:
    if czy_nawiasy_się_zgadzają_w_tym_ciągu_znaków(linia):
        print("TRUE")
    else:
        print("FALSE")