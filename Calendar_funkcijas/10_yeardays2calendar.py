#Biblotekas importēšana
import calendar

obj = calendar.Calendar()

year = 2016
# default value of width is 3

# printing with yeardays2calendar
print(obj.yeardays2calendar(year, 3))

"""
yeardays2calendar(year, width=3)
Atgriež datus par katru mēnesi, kur katrs mēnesis ir saraksts ar nedēļām. Pirmais  atgrieztais skaitlis ir datums, otrais- nedēļas dienas numurs (0-6). Vietās, kur datuma nummurs ir 0, tiek attēlotas dienas pirms un pēc mēneša.
Ievades vērtība year nosaka, kuru gadu attēlot. Ievades vērtība width nosaka, cik mēnešu jāiekļauj katrā rindiņā kalendārā. (Noklusējuma vērtība ir 3.)
"""
