from datetime import datetime, timedelta

class Skiftlag:
    def __init__(self, namn, startperiod, ref_datum):
        self.namn = namn
        self.startperiod = startperiod
        self.ref_datum = ref_datum

    def __str__(self) -> str:
        return self.namn

def lon_summa(datum1, datum2, ref_datum, start_period): #lönnesumma uträknad från ett referensdatum till ett slutdatum
    
    if datum1 < ref_datum :
        raise ValueError("Datumet är innan referensdatumet")

    summa = 0
    period = start_period
    dag_iter = 0

    while ref_datum < datum2:

        if ref_datum == datum1:
            summa1 = summa

        if dag_iter < len(p_tot[period]):
            summa += p_tot[period][dag_iter]

        if period == 0:
            ledig = 3
        else:
            ledig = 4

        dag_iter = (dag_iter + 1) % (len(p_tot[period]) + ledig +1)
        
        if dag_iter == 0:
            period = (period + 1) % 3
        
        ref_datum += timedelta(days=1)

       
        
    return summa - summa1

def main():


    for i in range(len(skiftlag)):
        print(i+1, skiftlag[i])
    
    x = int(input("Välj skiftlag 1-5: "))

    skift = skiftlag[x-1]

    datum1 = input("Ange startdatum enl. åååå-mm-dd: ")
    datum1 = datum1.split("-")
    datum2 = input("Ange slutdatum enl. åååå-mm-dd: ")
    datum2 = datum2.split("-")

    start_datum = datetime(int(datum1[0]), int(datum1[1]), int(datum1[2]))
    slut_datum = datetime(int(datum2[0]), int(datum2[1]), int(datum2[2]))

    summa = lon_summa(start_datum, slut_datum, skift.ref_datum, skift.startperiod)

    print(f"Intjänade pengar: {round(summa*1.12)} kr \nNetto: {round(summa*1.12*0.67)}")

skftlg = 1.1025
gl = 203.99*skftlg
ob1 = 28.57
ob2 = 57.32
ob3 = 79.95
atf = 7.91

fmvar = 8.20*gl + 0.5*ob2 + 8.20*atf
fmhelg = 8.20*gl + 0.50*ob2 + 8.20*ob3 + 8.20*atf

emvar = 8.20*gl + 5.70*ob1 + 8.20*atf
emhelg = 8.20*gl + 5.70*ob1 + 8.20*ob3 + 8.20*atf

nattvar = 8.20*gl + 0.50*ob1 + 7.70*ob2 + 8.20*atf
nattfre = 8.20*gl + 0.50*ob1 + 7.70*ob2 + 7.70*ob3 + 8.20*atf
nattlor = 8.20*gl + 0.50*ob1 + 7.70*ob2 + 8.20*ob3 + 8.20*atf
nattson = 8.20*gl + 0.50*ob1 + 7.70*ob2 + 0.50*ob3 + 8.20*atf

p1 = [fmvar, fmvar, emvar, emvar, nattfre, nattlor, nattson]
p2 = [fmhelg, fmhelg, fmhelg, emvar, emvar, nattvar, nattvar]
p3 = [fmvar, fmvar, emhelg, emhelg, emhelg, nattvar, nattvar]

p_tot = [p1, p2, p3]

a = Skiftlag("a", 2, datetime(2023, 1, 16))
b = Skiftlag("b", 2, datetime(2023, 1, 23))
c = Skiftlag("c", 2, datetime(2023, 1, 30))
d = Skiftlag("d", 2, datetime(2023, 1, 9))
e = Skiftlag("e", 2, datetime(2023, 1, 2))

skiftlag = [a, b, c, d, e]

main()

