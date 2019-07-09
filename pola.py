#!/usr/bin/python3

import math

def kwadrat():
    print("Policzmy pole kwadratu.\n ")
    a = float(input("Podaj długość boku:\n "))
    return a ** 2

def kolo():
    print("Policzmy pole koła. ")
    r = float(input("Podaj długość promienia:\n "))
    return math.pi * (r ** 2)

def trojkat():
    print("Policzmy pole trójkąta. ")
    at = float(input("Podaj długość podstawy trójkąta:\n "))
    h = float(input("Podaj długość wysokości trójkąta, opuszczonej na jego podstawę:\n "))
    return at * h * 0.5

def prostokat():
    print("Policzmy pole prostokąta. ")
    ap = float(input("Podaj długość pierwszego boku prostokąta\n"))
    b = float(input("Podaj długość drugiego boku prostokąta\n"))
    return ap * b

c = '0'

while (c != 'k' or c != 'K'):
    c = input("Wybierz pole jakiej figury chcesz obliczyć: 1 - kwadrat, 2 - koło, 3 - trójkąt, 4 - prostokąt, k - aby zakończyc. \n")
    if (c == 'k' or c == 'K'):
        break
    elif (c == '1'):
        wynik = kwadrat()
    elif (c == '2'):
        wynik = kolo()
    elif (c == '3'):
        wynik = trojkat()
    elif (c == '4'):
        wynik = prostokat()
    else:
        print("Dokonałeś złego wyboru spróbuj jeszcze raz. ")
        continue
    if (c == '1'):
        napis = "kwadratu"
    elif (c == '2'):
        napis = "koła"
    elif (c == '3'):
        napis = "trójkąta"
    elif (c == '4'):
        napis = "prostokąta"
    print("Pole " + napis + " wynosi: ", wynik)

print("The End!!!")
