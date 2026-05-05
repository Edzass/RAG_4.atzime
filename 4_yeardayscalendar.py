
import calendar

obj = calendar.Calendar()

# iterating with yeardayscalendar
for day in obj.yeardayscalendar(2018, 1):
    print(day)

"""
yeardayscalendar(year, width=3)
Atgriež iteratoru ar datiem par katru mēnesi, kur katrs mēnesis ir saraksts ar nedēļām, un katra nedēļa ir saraksts ar dienām. Dienas, kas pieder iepriekšējam vai nākamajam mēnesim, tiek attēlotas kā 0.
"""