import calendar
tc= calendar.TextCalendar(firstweekday=0)
print(tc.pryear(2016, 5))

"""
pryear(year, w=0, l=0)
Atgriež gada kalendāru kā tekstu. Parametri w un l nosaka, cik rakstzīmju platums un cik rindu augstums ir katrai dienai. Noklusējuma vērtība ir 0, kas nozīmē, ka tiek izmantots minimālais nepieciešamais platums un augstums.
"""