import calendar


print("Kāda ir pirmā nedēļas diena?")
print("Pirmdiena(0) ; Otrdiena(1) ; Trešdiena(2) ; Ceturtdiena(3) ; Piektdiena(4) ; Sestdiena(5) ; Svētdiena(6)")

first_day = 0
cal = calendar.Calendar(firstweekday=first_day)

print(f"\nJūs norādījāt, nedēļas pirmā diena ir: {cal.getfirstweekday()}")

"""
setfirstweekday(firstweekday)
Funkcija ļauj ievadīt un saglabāt , pretēji - izvadīt, nedēļas pirmo dienu kā skaitli. Nedēļas dienu numuri ir attēloti 0 (pirmdiena), 1(otrdiena), 2(trešdiena), 3(ceturtdiena), 4(piektdiena), 5(sestdiena), 6(svētdiena).
"""