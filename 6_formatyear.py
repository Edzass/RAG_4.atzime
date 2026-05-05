
import calendar

text_cal = calendar.TextCalendar(firstweekday = 0)

year = 2018
width = 4

print(text_cal.formatyear(year, width))

"""
formatyear(year, width=2)
Atgriež gada kalendāru kā tekstu. Parametrs width nosaka, cik rakstzīmju platums ir katrai dienai. Noklusējuma vērtība ir 2, kas nozīmē, ka tiek izmantots minimālais nepieciešamais platums.
"""