# Python program to demonstrate working of formatmonth() method

# importing calendar module
import calendar

text_cal = calendar.HTMLCalendar(firstweekday = 0)


# printing formatmonth
print(text_cal.formatmonth(2018, 9, withyear = True))

"""
formatmonth(year, month, withyear=True)
Atgriež mēneša kalendāru kā HTML tabulu. Parametrs withyear nosaka, vai kalendārā jāiekļauj gads. Noklusējuma vērtība ir True, kas nozīmē, ka gads tiks iekļauts.
"""
