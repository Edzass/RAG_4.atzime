
import calendar

text_cal = calendar.TextCalendar(firstweekday = 0)

year = 2018
width = 4

print(text_cal.formatyear(year, width))

"""
formatyear(year, width=2)
Atgriež gada pilno kalendāru kā tekstu. 
Ievades vērtība width nosaka, cik rakstzīmju platums ir katrai dienai. (Noklusējuma vērtība ir 2.) Ievades vērtība year nosaka, kuru gadu attēlot.
"""