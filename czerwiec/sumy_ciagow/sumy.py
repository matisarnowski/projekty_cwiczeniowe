#!/usr/bin/python3.7

import math

def liczby_naturalne (n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

def liczby_naprzemienne (b):
    suma = 0
    if b == 1:
        suma = 1
    else:
        suma = 1
        for i in range(2, b + 1):
            if i % 2 == 0:
                suma += i
            else:
                suma -= i
    return suma

def liczby_nieparzyste (v):
    suma = 0
    for i in range(1, v + 1):
        if i % 2 == 1:
            suma += i
    return suma

def liczba_razy (l):
    suma = 0
    for i in range(1, l + 1):
        suma += i*(i + 1)
    return suma

def ulamki (c):
    suma = 0
    for i in range(1, c + 1):
        suma += 1/i
    return suma

def ulamki_naprzemienne (b):
    suma = 0
    if b == 1:
        suma = 1
    else:
        suma = 1
        for i in range(2, b + 1):
            if i % 2 == 0:
                suma += 1/i
            else:
                suma -= 1/i
    return suma

def ulamek_pier (x):
    suma = 0
    for i in range(1, x + 1):
        suma += (2*i)/math.sqrt(2*i + 1)
    return suma

def kwadrat (z):
    suma = 0
    for i in range(1, z + 1):
        suma += i*i
    return suma

liczba = int(input("Podaj liczbę naturalną dla której chcesz wyliczyć sumy ciągów: "))

print("1 + 2 + 3 + 4 + ... + n = " + str(liczby_naturalne(liczba)))

print("1 + 2 - 3 + 4 - ... +/- n = " + str(liczby_naprzemienne(liczba)))

print("1 + 3 + 5 + 7 + ... + (2n - 1) = " + str(liczby_nieparzyste(liczba)))

print("1*2 + 2*3 + 3*4 + 4*5 + ... + n*(n + 1) = " + str(liczba_razy(liczba)))

print("1 + 1/2 + 1/3 + 1/4 + ... + 1/n = " + str(ulamki(liczba)))

print("2/sqrt(3) + 4/sqrt(5) + 6/sqrt(7) + ... + 2n/sqrt(2n + 1) = " + str(ulamek_pier(liczba)))

print("1**2 + 2**2 + 3**2 + 4**2 + ... + n**2 = " + str(kwadrat(liczba)))

