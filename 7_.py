
import calendar

obj = calendar.Calendar(firstweekday = 2)

# iterating with parameter itermonthdays2
for day in obj.itermonthdays2(2018, 9):
    print(day)

""" 
itermonthdays2(year, month)
Atgriež iteratoru ar visām mēneša dienām un to nedēļas dienu numuriem. Tas iekļauj arī papildu dienas pirms un pēc mēneša, lai izveidotu pilnas nedēļas. Nedēļas dienu numuri ir no 0 (pirmdiena) līdz 6 (svētdiena).
"""