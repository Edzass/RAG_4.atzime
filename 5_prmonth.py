
import calendar

text_cal = calendar.TextCalendar(firstweekday = 0)

year = 2018
month = 9


print(text_cal.prmonth(year, month))

"""
prmonth(year, month, w=0, l=0)
Atgriež mēneša kalendāru kā tekstu. Parametri w un l nosaka, cik rakstzīmju platums un cik rindu augstums ir katrai dienai. Noklusējuma vērtība ir 0, kas nozīmē, ka tiek izmantots minimālais nepieciešamais platums un augstums.
"""