
from calendar import Calendar

obj = Calendar()

for day in obj.itermonthdates(2018, 9):
    print(day)

""" 
itermonthdates(year, month)
Atgriež datus ar visām norādītā kalendārā mēneša dienām (Formāts gads, mēnesis, datums) Tas iekļauj arī dienas pirms un pēc noteiktā mēneša, līdzīgi kā redzams digitālajā kalendārā - mēneša sākumā vai beigās.
"""