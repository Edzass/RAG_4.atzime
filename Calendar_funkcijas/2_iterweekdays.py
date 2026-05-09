#Biblotekas importēšana
import calendar

obj = calendar.Calendar(firstweekday = 0)

#Iteratora izsaukšana
for day in obj.iterweekdays():
    print(day)


"""
iterweekdays()
Atgriež iteratoru ar nedēļas dienu numuriem vienai nedēļai. Pirmā vērtība sakrīt ar firstweekday īpašības vērtību.
"""