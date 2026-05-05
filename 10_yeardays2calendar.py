# Python program to demonstrate working
# of yeardays2calendar() method

# importing calendar module
import calendar

obj = calendar.Calendar()

year = 2016
# default value of width is 3

# printing with yeardays2calendar
print(obj.yeardays2calendar(year))

"""
yeardays2calendar(year, width=3)
Atgriež iteratoru ar datiem par katru mēnesi, kur katrs mēnesis ir saraksts ar nedēļām, un katra nedēļa ir saraksts ar dienām. Katrs datums tiek attēlots kā tuple, kur pirmais elements ir dienas numurs, otrais elements ir nedēļas dienas numurs (no 0 līdz 6), un trešais elements ir gads. Dienas, kas pieder iepriekšējam vai nākamajam mēnesim, tiek attēlotas kā (0, 0, year).
"""
