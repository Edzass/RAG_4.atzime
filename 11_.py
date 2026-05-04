# Python program to demonstrate working
# of yeardatescalendar() method

# importing calendar module
import calendar

obj = calendar.Calendar()

year = 2016
# default value of width is 3

# printing with yeardatescalendar
print(obj.yeardatescalendar(year))

""" 
yeardatescalendar(year, width=3)
Atgriež iteratoru ar datiem par katru mēnesi, kur katrs mēnesis ir saraksts ar nedēļām, un katra nedēļa ir saraksts ar dienām. Katrs datums tiek attēlots kā datetime.date objekts. Dienas, kas pieder iepriekšējam vai nākamajam mēnesim, tiek attēlotas kā datetime.date objekts ar gadu, mēnesi un dienu iestatītu uz 1.
"""