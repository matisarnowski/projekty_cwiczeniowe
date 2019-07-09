#!/usr/bin/python3

import sys

print("To jest program, który pobierze od Ciebie dwie liczby. Większą z nich zawsze podzieli przez mniejszą.")

a = float(input("Podaj pierwszą liczbę wymierną.\n"))
b = float(input("Podaj drugą liczbę wymierną.\n"))

if (a >= b and b != 0):
    wynik = a / b
elif (a >= b and b == 0):
    print("Nie wolno dzielić przez zero. Kończymy program.")
    sys.exit()
elif (b >= a and a != 0):
    wynik = b / a
elif (b >= a and a == 0):
    print("Nie wolno dzielić przez zero. Kończymy program.")
    sys.exit()

print("Uzyskany wynik dzielenia, to: ", wynik)
print("Jak widać wynik zawsze będzie nie mniejszy od jedności.")
