# Python program to illustrate the 
# use of itermonthdays3() method

# import class
import calendar

# Creating Calendar Instance
cal = calendar.Calendar()
year = 2019
month = 12

print("Iterating over the weeks of December 2019 where each tuple is date, month and year")
for i in cal.itermonthdays3(year, month):
    print(i)
# first value is the day of the month; 
# days outside of the month is 0
# second value is weekday number where 
# Monday is 0 till Sunday which is 6
print()
print()

# set the firstweekday to 1
cal = calendar.Calendar(firstweekday = 1)
year = 1994
month = 9

print("Iterating over the weeks of September 1994 where each tuple is date, month and year and iterator starts with firstweekday as Tuesday")
for i in cal.itermonthdays3(year, month):
    print(i)
print()
print()

"""   
itermonthdays3(year, month)
Atgriež iteratoru ar visām mēneša dienām, to nedēļas dienu numuriem un gadu. Tas iekļauj arī papildu dienas pirms un pēc mēneša, lai izveidotu pilnas nedēļas. Nedēļas dienu numuri ir no 0 (pirmdiena) līdz 6 (svētdiena).
"""