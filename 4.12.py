n = 56
czynniki = []

while n != 1:
    for dzielnik in range(2, n + 1):
        while n % dzielnik == 0:
            czynniki.append(dzielnik)
            n //= dzielnik

print(tuple(czynniki))
