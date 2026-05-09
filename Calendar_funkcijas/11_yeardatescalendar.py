# Python program to demonstrate working
# of yeardatescalendar() method

# importing calendar module
import calendar

obj = calendar.Calendar()

year = 2016
# default value of width is 3

# printing with yeardatescalendar
print(obj.yeardatescalendar(year))

""" 
yeardatescalendar(year, width=3)
Atgriež datus par katru mēnesi gadā. Tiek atgriezts gads, mēnesis un datums. Teik iekļautas arī dienas pirms un pēc mēneša..
Ievades vērtība year nosaka, kuru gadu attēlot. Ievades vērtība width nosaka, cik mēnešu jāiekļauj katrā rindkopā. (Noklusējuma vērtība ir 3.)
"""