
bibloteka = {
    "1": "1_setfirstweekday.py", "2": "2_iterweekdays.py","3": "3_itermonthdays.py",
    "4": "4_yeardayscalendar.py", "5": "5_prmonth.py","6": "6_formatyear.py",
    "7": "7_itermonthdays2.py","8": "8_itermonthdays3.py","9": "9_itermonthdays4.py",
    "10": "10_yeardays2calendar.py", "11": "11_yeardatescalendar.py", "12": "12_formatmonth.py",
     "13": "13_pryear.py", "14": "14_isleap.py", "15": "15_weekheader.py"
}

skaitlis = input("Ievadi skaitli no 1 līdz 15: ").strip()
if skaitlis in bibloteka:
    fails = bibloteka[skaitlis]
    with open(f"Calendar_funkcijas/{fails}", encoding='utf-8') as file:
        exec(file.read())