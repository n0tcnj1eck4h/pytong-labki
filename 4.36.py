import random


# zakładamy że tablice mają takie same długości
def dodaj_elementy(a, b):
    w = []
    for i in range(len(a)):
        w.append(a[i] + b[i])
    return w


def odejmij_elementy(a, b):
    w = []
    for i in range(len(a)):
        w.append(a[i] - b[i])
    return w


def pomnoz_elementy(a, b):
    w = []
    for i in range(len(a)):
        w.append(a[i] * b[i])
    return w


def podziel_elementy(a, b):
    w = []
    for i in range(len(a)):
        w.append(a[i] / b[i])
    return w


def iloczyn_kartezjanski(a, b):
    suma = 0
    for i in a:
        for j in b:
            suma += i * j
    return suma


def pomnoz_elementy_przez(tab, x):
    w = []
    for v in tab:
        w.append(v * x)
    return w

n = 10
A = []
B = []

for i in range(n):
    A.append(random.randint(0, 100))
    B.append(random.randint(0, 100))

print("A = ", A)
print("B = ", B)
print("A + B = ", dodaj_elementy(A, B))
print("A - B = ", odejmij_elementy(A, B))
print("A * B = ", pomnoz_elementy(A, B))
print("A / B = ", podziel_elementy(A, B))
print("A × B = ", iloczyn_kartezjanski(A, B))
print("A × 5 = ", pomnoz_elementy_przez(A, 5))
print("A / 5 = ", pomnoz_elementy_przez(A, 1 / 5))
