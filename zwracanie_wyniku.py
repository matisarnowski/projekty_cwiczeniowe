#!/usr/bin/python3

import math
import os

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return(a * b)

def potegowanie(a, b):
    return a ** b

def pierwiastek(a, b):
    a = abs(a)
    return a ** (1 / b)

print("Witaj w kalkulatorze wykonującym rózne działania matematyczne, na liczbach wymiernych. ")

c = '0'

while(c != 'k' or c != 'K'):

    c = input("Wybierz: 1 - aby dodać; 2 - aby odjąć; 3 - aby pomnożyć; 4 - aby podzielić; 5 - aby potęgować; 6 - aby wyciągnąć pierwiastek, k - aby zakończyć.\n")

    if (c == 'k' or c == 'K'):
        break

    a = float(input("Wprowadź pierwszą liczbę, względem, której będziesz chciał wykonać działanie:\n"))
    b = float(input("Wprowadź drugą liczbę względem, której będziesz chciał wykonąć działanie. W wypadku potęgowania jest to wykładnik. W wypadku pierwiastkowania jest to stopień.\n"))
    
    if (c == '1'):
        wynik = dodawanie(a, b)
    elif (c == '2'):
        wynik = odejmowanie(a, b)
    elif (c == '3'):
        wynik = mnozenie(a, b)
    elif (c == '4'):
        if (b != 0):
             wynik = dzielenie(a, b)
        else:
             print("Nie można dzielić przez zero, to niewybaczalny błąd. Zaczynamy jeszcze raz.")
             continue
    elif (c == '5'):
        wynik = potegowanie(a, b)
    elif (c == '6'):
        if (a >= 0 and b % 2 == 0):
             wynik = pierwiastek(a, b)
        elif (a < 0 and b % 2 == 0):
             print("Nie można wyciągać pierwiastkóœ o stopniu parzystym z liczb ujemnych rozwiązując działanuie w liczbach rzezcywistych. Skorzystaj z bardziej zaawansowanego kalkulatora")
             continue
        elif (a >= 0 and b % 2 == 1):
            wynik = pierwiastek(a, b)
           
    print("Wynik działania, to: ", wynik)
    continue
    
print("THE END!!!")
