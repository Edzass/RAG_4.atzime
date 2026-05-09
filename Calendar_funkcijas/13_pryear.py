import calendar
tc= calendar.TextCalendar(firstweekday=0)
print(tc.pryear(2016, 5))

"""
pryear(theyear, w=2, l=1, c=6, m=3)
Atgriež pilnu gada kalendāru kā tekstu. 
Ievades vērtība theyear nosaka, kuru gadu attēlot; w - cik rakstzīmju platums ir katrai dienai(Noklusējuma vērtība ir 2.); l - cik rindu jāizmanto katram mēnesim(Noklusējuma vērtība ir 1.);  c - cik rakstzīmju platums ir katram mēneša nosaukumam. (Noklusējuma vērtība ir 6.); m - cik mēnešu jāiekļauj katrā rindiņā. (Noklusējuma vērtība ir 3.)
"""