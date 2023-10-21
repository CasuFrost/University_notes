import math


def drawCorenrLine():
    print("+ - - - - + - - - - +")
def drawLine():
    print("|         |         |")
def drawRect():
    num = [0,1,2,3]
    drawCorenrLine()
    for i in num:
        drawLine()
    drawCorenrLine()
    for i in num:
        drawLine()
    drawCorenrLine()

drawRect()
#Scrivere una funzione che prende un numero in virgola mobile, ne calcola la radice cubica, e la ritorna.
def radiceCubica(a):
    return a**(1/3)


#Scrivere una funzione che prende tre numeri in virgola mobile ( a , b , c ) e calcola le radici dell'equazione a x^2 + b x
#+ c e ritorna la maggiore. Modificare poi la funzione per ritornare entrambi i valori.

def formulaRIsuolutivaHigher(a,b,c):
    xUno = (-b+math.sqrt((b**2-4*(a*c))))/2*a
    xDue = (-b-math.sqrt((b**2-4*(a*c))))/2*a
    if xUno > xDue:
        return xUno
    return xDue


def formulaRIsuolutiva(a,b,c):
    xUno = (-b+math.sqrt((b**2-4*(a*c))))/2*a
    xDue = (-b-math.sqrt((b**2-4*(a*c))))/2*a
    xUnoString = str(xUno)
    xDueString = str(xDue)
    return xUnoString+" "+xDueString


#Scrivere una funzione che prende come input cinque numeri e ritorna la somma dei numeri pari meno quella dei numeri
#dispari.   

def pariPiùDispari(a):
    listaNumeri = list(a)
    sommaPari = 0
    sommaDispari = 0
    for x in a:
        numero = int(x)
        if numero%2==0:
            sommaPari+=numero
        else:
            sommaDispari+=numero
            
    return sommaPari-sommaDispari


#Scrivere una funzione che prende tre valori di input, e ritorna la loro somma se i valori sono punteggi di esame validi ( 0
#<= grade <= 30 ), e altrimenti ritorna -1 . Scriverne poi una variante che legge i valori da terminale con input .
def votoEsame(a,b,c) :
    somma = a+b+c
    if somma >= 0 and somma <=30:
        return somma
    return -1


#Scrivere una funzione che prende tre valori ( d , m , y ) e ritorna se la data è valida o no. Si possono ignorare gli anni
#bisestili. Ad esempio, ritorna False per 30/2/2017 e True per 1/1/1111 .
def isAValidDay(d,m,y):
    if m >= 1 and m <= 12:
        if m == 9 or m == 11 or m == 6 or m == 4:
            if d >= 1 and d <= 30:
                return True
        elif m == 2:
            if d >= 1 and d <= 28:
                return True
        else:
            if d >= 1 and d <= 31:
                return True
    return False


#Scrivere una funzione che implenta la stessa funzionalità di str.strip()    
def Strip(s):
    cnt = 0
    lista = list(s)
    for x in lista:
        cnt+=1
        
    if lista[cnt-1] == " ":
       lista[cnt-1]=""
    if lista[0] == " ":
       lista[0]=""
    stringStrippata=""
    for x in lista:
        stringStrippata+=x
    return stringStrippata

#Scrivere una funzione che ritorna una stringa di saluto formata da Ciao , seguito dal nome letto come input e poi da
#Buona giornata!
def saluto():
    print("inserisci il tuo nome : ")
    nome = input()
    print("Ciao ",nome," Buona giornata!")

secondi = 42*60+42
minuti = 42+42/60
migliaIn10Km = 10/1.61
#Scrivete una espressione che calcoli il numero di secondi che ci sono in 42 minuti e 42 secondi.
print("Numero di secondi in 42 minuti e 42 secondi : ",secondi) 
#Scrivete una espressione che calcoli il numero di miglia che ci sono in 10 chilometri. (1 miglio = 1.61 km).
print("10 km in miglia sono : ",migliaIn10Km)
#Scrivete una espressione che calcoli la velocità media e la cadenza media (tempo per miglio, in minuti e secondi) di un
#corridore che corre una gara di 10 chilometri in 42 minuti e 42 secondi.
print("")
print("un corridore corre ",migliaIn10Km," miglia in ",secondi," secondi, la sua cadenza media è di ",migliaIn10Km/secondi," miglia al secondo")
print("la sua velocità media è invece di ",migliaIn10Km/minuti," miglia al minuto")
#Il volume di una sfera di raggio r è 4/3 * PI * r^3 . Scrivere una espressione che calcoli il volume di una sfera di
#raggio 5.
print("")
print("il volume di una sfera di raggio 5 è ",(4/3)*math.pi*(5**3))

#Il prezzo di copertina di un libro è 24.95, ma una liberia ottiene il 40% di sconto. I costi di spedizione sono 3 euro per la
#prima copia, e 75 centesimi per ogni copia aggiuntiva. Qual'è il costo totale di 60 copie?
print("")
prezzoLibroScontato = 24.95-((24.95 *40)/100)
print("il costo totale di 60 copie è ",3+(59*0.75)+60*prezzoLibroScontato," euro")
#Se uscite di casa alle 6:52 di mattina e correte un miglio a ritmo blando (8 minuti e 15 secondi al miglio), e poi 3 miglia a
#ritmo moderato (7 minuti e 12 secondi al miglio), e infine un altro miglio a ritmo blando (9 minuti e 45 secondi al miglio), a
#che ora sarete tornati a casa?
print("")
oreInizioCorsa = 6
minutiInizioCorsa = 52
MinutiTreMigliaAlRitmoBlando = 8
SecondiTreMigliaAlRitmoBlado = 15
MinutiTreMigliaAlRitmoBlandoDue = 9
SecondiTreMigliaAlRitmoBladoDue = 45
MinutiTreMigliaAlRitmoModerato = 7*3
SecondiTreMigliaAlRitmoModerato = 12*3
MinutiTotaliCorsa = MinutiTreMigliaAlRitmoBlando+MinutiTreMigliaAlRitmoBlandoDue+MinutiTreMigliaAlRitmoModerato
SecondiTotaliCorsa = SecondiTreMigliaAlRitmoBlado+SecondiTreMigliaAlRitmoModerato+SecondiTreMigliaAlRitmoBladoDue
while SecondiTotaliCorsa>60:
    SecondiTotaliCorsa-=60
    MinutiTotaliCorsa+=1

oreFineCorsa = oreInizioCorsa
minutiFineCorsa=MinutiTotaliCorsa+minutiInizioCorsa
while minutiFineCorsa>60:
    oreFineCorsa+=1
    minutiFineCorsa-=60
print("La corsa inizia alle 6:52 dura in totale ",MinutiTotaliCorsa,":",SecondiTotaliCorsa," torniamo a casa alle : ",oreFineCorsa,":",minutiFineCorsa)

#Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale. Ad esempio, s="85721" . Stampate la somma delle
#cifre contenute nella stringa.
print("")
print("inserire stringa di numeri")

stringaCaratteri = input()
listaCaratteri = list(stringaCaratteri)
res = 0
for x in listaCaratteri:
    res+=int(x)
print("la somma di tutti i numeri contenuti nella stringa è ",res)

#Scrivete una espressione che a partire da una stringa di 5 caratteri, rappresentante un numero binario, stampi la sua
#rappresentazione decimale. Ad esempio, s="00101" -> 5 .
print("inserire numero binario")
binario = input()
listaNumeri = list(binario)
decimale=0
bits = len(listaNumeri)-1
for i in listaNumeri:
    decimale+=int(i)*(2**bits)
    bits-=1
print(decimale)
print("")

#Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale ('.'). Ad esempio, s="52.29". Stampare il numero
#decimale rappresentato dalla stringa (stamparlo come numero, non come stringa).
DecimalNumberInString = "72.35"
print("stringa in float = ",float(DecimalNumberInString))
print("")



        


