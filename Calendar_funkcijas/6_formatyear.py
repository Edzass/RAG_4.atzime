
import calendar

html_cal = calendar.HTMLCalendar(firstweekday = 0)

year = 2018
width = 4

print(html_cal.formatyear(year, width))

"""
formatyear(year, width=2)
Atgriež gada pilno kalendāru kā HTML tabulu. 
Ievades vērtība width nosaka, cik meneši tiek attēloti katrā rindā. (Noklusējuma vērtība ir 3.) Ievades vērtība year nosaka, kuru gadu attēlot.
"""