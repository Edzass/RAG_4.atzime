import calendar

obj = calendar.Calendar(firstweekday = 0)

for day in obj.iterweekdays():
    print(day)


"""
iterweekdays()
Atgriež datus ar nedēļas dienu numuriem vienai nedēļai. Pirmā vērtība sakrīt ar firstweekday īpašības vērtību.
"""