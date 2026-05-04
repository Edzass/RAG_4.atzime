import calendar


print("Kāda ir pirmā nedēļas diena?")
print("Pirmdiena(1) ; Otrdiena(2) ; Trešdiena(3) ; Ceturtdiena(4) ; Piektdiena(5) ; Sestdiena(6) ; Svētdiena(7)")

first_day = int(input("Ievadi numuru: "))
cal = calendar.Calendar(firstweekday=first_day)

print(f"\nJūs norādījāt, nedēļas pirmā diena ir: {cal.getfirstweekday()}")

"""
setfirstweekday(firstweekday)
Funkcija ļauj ievadīt un saglabāt , pretēji - izvadīt, nedēļas pirmo dienu kā skaitli.
"""