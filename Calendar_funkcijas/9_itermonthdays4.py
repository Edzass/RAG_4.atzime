import calendar

cal = calendar.Calendar()
days = cal.itermonthdays4(2022, 2)

for day in days:
    print(day)

"""
itermonthdays4(year, month)
Atgriež datus ar visām norādītā mēneša datumiem, to nedēļas dienu numuriem, nedēļu numuriem un gadu. Tas iekļauj arī papildu dienas pirms un pēc mēneša. 
Ievades vērtība year nosaka, kuru gadu attēlot, month- kuru mēnesi attēlot.  
"""