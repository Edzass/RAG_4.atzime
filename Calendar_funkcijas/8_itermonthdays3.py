# Python program to illustrate the 
# use of itermonthdays3() method

# import class
import calendar

cal = calendar.Calendar(firstweekday = 1)
year = 2026
month = 9

for i in cal.itermonthdays3(year, month):
    print(i)
print()


"""   
itermonthdays3(year, month)
Atgriež datus ar visām izvēlētajām mēneša dienām, mēnesi un gadu. Tiek iekļautas arī papildu dienas pirms un pēc mēneša, lai izveidotu pilnas nedēļas.
Ievades vērtība year nosaka, kuru gadu attēlot. Ievades vērtība month nosaka mēnesi attēlot, kuru attēlot.
"""