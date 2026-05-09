
import calendar

obj = calendar.Calendar()

# iterating with yeardayscalendar
for day in obj.yeardayscalendar(2018, 1):
    print(day)

"""
yeardayscalendar(year, width=3)
Atgriež datus par visa gada mēnešiem, kur katrs mēnesis ir saraksts ar nedēļām, un katra nedēļa ir saraksts ar dienām. Dienas, kas pieder iepriekšējam vai nākamajam mēnesim, tiek attēlotas kā "0" vērtības.
Pirmais ievades lauks apzīmē gadu, bet otrais ievades lauks apzīmē mēneša datu attēlojuma platumu.
"""