Pamatojums:
Es esmu izvēlējies Calendar bibliotēku, jo, manuprāt, tās ir pamats dažādās programmās un spēlēs izmantot dažādus notikumus un pieejamās iespējas atkarībā no datuma, mēneša un gada. Bibliotēka nodrošina gatavas funkcijas dažāda veida pielāgotu kalendāru izveidei, dienu nosaukumu attēlošanai un nedēļu skaitīšanai.

Bibliotēkas ieguvumi:
Pēc noklusējuma iebūvēta Python— nav nepieciešama papildu instalēšana; ir iespējams ātri izveidot mēneša vai gada kalendāru; iespējami dažādi informācijas izvades formāti — teksts vai HTML; vienkārši uztverami datu ievades lauku skaidrojumi ; Bibliotēka var ātri noteikt nedēļas dienu nummurus, nedēļu nummurus, mēnešu nummurus lielākam datu apjomam.

Bibliotēkas ierobežojumi:
Ierobežotas dizaina un pielāgošanas iespējas, jo īpaši teksta formātā; sarežģītākiem datumu aprēķiniem nepieciešama datetime bibliotēka; ierobežotas iespējas darbam ar laika joslām; neatbalsta automātisku sasaisti "vai sinhronizāciju ar ārējiem servisiem.

FUNKCIJU SKAIDROJUMI:

setfirstweekday(firstweekday)
Funkcija ļauj ievadīt un saglabāt , pretēji - izvadīt, nedēļas pirmo dienu kā skaitli. (0 - pirmdiena, 6 - svētdiena)

iterweekdays()
Atgriež iteratoru ar nedēļas dienu numuriem vienai nedēļai. Pirmā vērtība sakrīt ar firstweekday īpašības vērtību.

itermonthdates(year, month)
Atgriež datus ar visām norādītā kalendārā mēneša dienām (Formāts gads, mēnesis, datums) Tas iekļauj arī dienas pirms un pēc noteiktā mēneša, līdzīgi kā redzams digitālajā kalendārā - mēneša sākumā vai beigās.

yeardayscalendar(year, width=3)
Atgriež datus par visa gada mēnešiem, kur katrs mēnesis ir saraksts ar nedēļām, un katra nedēļa ir saraksts ar dienām. 

prmonth(year, month, w=0, l=0)
Atgriež mēneša kalendāru kā tekstu - dienas tiek attēlotas kā skaitļi, tomēr blaus esošo mēnešu datumi tiek attēloti kā atstarpes.

formatyear(year, width=2)
Atgriež gada pilno kalendāru kā HTML tabulu. 

itermonthdays2(year, month)
Atgriež datus ar visām mēneša dienām un to nedēļas dienu numuriem, tiek iekļautas arī  dienas pirms un pēc mēneša - kas tiek apzīmētas ar "0" vērtībām. 

itermonthdays3(year, month)
Atgriež datus ar visām izvēlētā mēneša dienām, mēnesi un gadu. Tiek iekļautas arī papildu dienas pirms un pēc mēneša, lai izveidotu pilnas nedēļas.

itermonthdays4(year, month)
Atgriež datus ar visām norādītā mēneša datumiem, to nedēļas dienu numuriem, nedēļu numuriem un gadu. Tas iekļauj arī papildu dienas pirms un pēc mēneša. 

yeardays2calendar(year, width=3)
Atgriež datus par katru mēnesi, kur katrs mēnesis ir saraksts ar nedēļām. Pirmais atgrieztais skaitlis ir datums, otrais- nedēļas dienas numurs (0-6). Vietās, kur datuma nummurs ir 0, tiek attēlotas dienas pirms un pēc mēneša.

yeardatescalendar(year, width=3)
Atgriež datus par katru mēnesi gadā. Tiek atgriezts gads, mēnesis un datums. Teik iekļautas arī dienas pirms un pēc mēneša.

formatmonth(year, month, withyear=True)
Atgriež mēneša kalendāru kā HTML dokumenta tabulu. 

pryear(theyear, w=2, l=1, c=6, m=3)
Atgriež pilnu gada kalendāru kā tekstu. 

isleap(year)
Pārbauda, vai norādītais gads ir garais gads. Garais gads ir dalāms ar 4, bet nav dalāms ar 100, izņemot gadījumus, kad tas ir dalāms ar 400.

weekheader(n)
Atgriež nedēļas dienu saīsinājumus kā virkni. 