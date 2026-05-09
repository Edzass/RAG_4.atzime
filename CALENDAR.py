
import tkinter as tk
import io
import sys

bibloteka = {
    "1": "1_setfirstweekday.py", "2": "2_iterweekdays.py","3": "3_itermonthdates.py",
    "4": "4_yeardayscalendar.py", "5": "5_prmonth.py","6": "6_formatyear.py",
    "7": "7_itermonthdays2.py","8": "8_itermonthdays3.py","9": "9_itermonthdays4.py",
    "10": "10_yeardays2calendar.py", "11": "11_yeardatescalendar.py", "12": "12_formatmonth.py",
     "13": "13_pryear.py", "14": "14_isleap.py", "15": "15_weekheader.py"
}

def palaist():

    output = io.StringIO()
    sys.stdout = output

    with open("Calendar_funkcijas/" + bibloteka[ievade.get()], encoding="utf-8") as file:
        exec(file.read())

    sys.stdout = sys.__stdout__

    teksts.delete("1.0", tk.END)
    teksts.insert(tk.END, output.getvalue())

logs = tk.Tk()
logs.title("Calendar_funkcijas")
logs.geometry("700x500")

tk.Label(logs, text="Ievadi skaitli no 1 līdz 15").pack()

ievade = tk.Entry(logs)
ievade.pack()

poga = tk.Button(logs, text="Palaist", command=palaist)
poga.pack()

teksts = tk.Text(logs)
teksts.pack()

logs.mainloop()