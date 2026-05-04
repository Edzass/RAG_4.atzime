import calendar

cal = calendar.Calendar()
days = cal.itermonthdays4(2022, 2)

for day in days:
    print(day)

"""
itermonthdays4(year, month)
Atgriež iteratoru ar visām mēneša dienām, to nedēļas dienu numuriem un gadu. Tas iekļauj arī papildu dienas pirms un pēc mēneša, lai izveidotu pilnas nedēļas. Nedēļas dienu numuri ir no 0 (pirmdiena) līdz 6 (svētdiena).
"""