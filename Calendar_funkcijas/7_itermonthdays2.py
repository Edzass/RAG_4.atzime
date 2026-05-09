
import calendar

obj = calendar.Calendar(firstweekday = 2)

# iterating with parameter itermonthdays2
for day in obj.itermonthdays2(2018, 9):
    print(day)

""" 
itermonthdays2(year, month)
Atgriež datus ar visām mēneša dienām un to nedēļas dienu numuriem, tiek iekļautas arī  dienas pirms un pēc mēneša - kas tiek apzīmētas ar "0" vērtībām. 
Ievades vērtība year nosaka, kuru gadu attēlot. Ievades vērtība month nosaka, kuru mēnesi attēlot.
"""