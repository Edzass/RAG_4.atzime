#Biblotekas importēšana
import calendar

text_cal = calendar.TextCalendar(firstweekday = 0)

year = 2018
month = 9

print(text_cal.prmonth(year, month))

"""
prmonth(year, month, w=0, l=0)
Atgriež mēneša kalendāru kā tekstu - dienas tiek attēlotas kā skaitļi, tomēr blaus esošo mēnešu datumi tiek attēloti kā atstarpes.
Ievades vērtības year un month nosaka, kuru mēnesi attēlot. 
"""