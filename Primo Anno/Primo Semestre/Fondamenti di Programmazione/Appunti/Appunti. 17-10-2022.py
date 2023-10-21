import math
def logaritmo_boh(N):
    return int(math.log10(N))+1

def cerca_numero():
    cifre=200
    i=1
    for i in range(1,200):
        X = logaritmo_boh(i)
        if X < cifre:
            cifre-=X
        else:
            return i,cifre

def cerca_senza_stringhe():
    pass

#le tuple sono sequenze non modificabili

#dizionari
D = {'2':3, 's':1}

#elenco dei valori
D.values()

#elenco degli oggetti chiave-valore
D.items()

#elenco delle chiavi
D.keys()

cnt=0
for number in range(101):
    if number%3 == 0 and number%4==0:
        cnt+=1
        print(number)
#quanti multipli di 3 che sono anche multipli di 4

#se non si sa quanti parametri si vogliono dare, si inserisca l'asterisco prima del parametro
def funzioneMultiParametro(*robeDastampare):
    pass


X = {11,52,13,49}
D = 1,2,*X,4
print(D)


#FUNZIONE RICORSIVA
#ogni funzione ricorsiva ha almeno una soluzione conosciuta(caso base),il problema può essere scomposto
#in problemi più piccoli, e a dorza di ridurre si casca sempre in uno dei casi base. Dalle soluzioni
#dei sottoproblei possiamo costruire la soluzione del problema
def Fattoriale(N):
    if N < 2:
        return 1
    else:
        return N * Fattoriale(N-1)
 
print(Fattoriale(1))

print(5--2)