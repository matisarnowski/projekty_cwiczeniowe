#!/usr/bin/python3

import sys
print("Witaj w prostym kalkulatorze!")

a = float(input("Wprowadź pierwszą, dowolną liczbę wymierną: "))
b = float(input("Wprowadź drugą, dowolną liczbę wymierną: "))

c = input("Wybierz rodzaj działania: 1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie: ")

if (c == '1'):
    wynik = a + b
elif (c == '2'):
    wynik = a - b
elif (c == '3'):
    wynik = a * b
elif (c == '4'):
    if (b != 0):
        wynik = a / b
    else:
        print("Nie można dzielić przez 0.")
        sys.exit()
else:
    print("Dokonałeś złego wyboru! ")

print("Wynik działania, to: ", wynik)
