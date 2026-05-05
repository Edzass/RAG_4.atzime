

from calendar import Calendar

obj = Calendar()

for day in obj.itermonthdates(2018, 9):
    print(day)

""" 
itermonthdays(year, month)
Atgriež iteratoru ar visām mēneša dienām. Tas iekļauj arī papildu dienas pirms un pēc mēneša, lai izveidotu pilnas nedēļas.
"""