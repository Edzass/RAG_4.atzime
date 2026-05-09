# Python program to demonstrate working of formatmonth() method

# importing calendar module
import calendar

text_cal = calendar.HTMLCalendar(firstweekday = 0)


# printing formatmonth
print(text_cal.formatmonth(2018, 9, withyear = True))

"""
formatmonth(year, month, withyear=True)
Atgriež mēneša kalendāru kā HTML dokumenta tabulu. 
Ievades vērtība year nosaka, kuru gadu attēlot; month- kuru mēnesi attēlot; withyear - vai kalendārā jāiekļauj gads (noklusējuma vērtība ir True).
"""
