import random


def arbitralna(N, zakres_dolny, zakres_gorny):
    liczby = []
    for i in range(N):
        liczby.append(random.randint(zakres_dolny, zakres_gorny))
    return liczby


print(arbitralna(10, 10, 90))
