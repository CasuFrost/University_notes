#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "MARCO"
cognome     = "CASU"
matricola   = "2046212"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla FINE di grade.py
#
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# DEBUG=True vi attiva anche lo STACK TRACE degli errori per sapere il numero
# di linea di program.py che genera l'errore.
################################################################################


# ----------------------------------- EX.1 ----------------------------------- #
"""
Esercizio 1: 6 punti

Si scriva una funzione ex1(Q, file_db, k) che prende in ingresso una
tupla Q, file_db che punta ad un file di testo, mentre k e' un
intero. Q e' una tupla (x, y) che indica le coordinate del punto di
query. Invece file_db contiene punti 2D su ogni riga. Ogni riga
contiene le coordinate intere x e y separate da uno spazio, come ad
esempio:

  -5 -5
  10 5

La funzione deve leggere il contenuto del file. Dato il punto Q, si
deve cercare gli indici dei k punti piu vicini a Q in file_db. Per la
distanza fra (x1, y1) e (x2, y2) si usi:
(x1-x2)² + (y1-y2)²

Ad esempio, se k=2 e Q=(-5, -5) e file_db contiene:

  1 1
  -3 -5
  -5 -3
  20 10

gli indici e le distanze di file_db rispetto a Q sono:

 | indice |  x |  y | dist |
 |      0 |  1 |  1 | 72   |
 |      1 | -3 | -5 | 4    |
 |      2 | -5 | -3 | 4    |
 |      3 | 20 | 10 | 850  |

I due vicini a Q sono la lista [2, 1] in quanto hanno le k=2 distanze
minori.  In caso di parita' sulla distanza, come in questo caso, si
ritornano gli indici dal piu grande al piu piccolo.

Si ritorni la lista che contiene i k indici vicini come sudetto.
Se in ingresso abbiamo Q=(-5, -5) e db_00.txt e k=2, si deve ritornare:

 [2, 1]

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""
def ordInDist(listIndexDist,k):
    #print(listIndexDist)
    for i in range(len(listIndexDist)):
        for j in range(len(listIndexDist)):
            #print(listIndexDist[i],listIndexDist[j])
            if i!=j:
                if listIndexDist[i][1]<listIndexDist[j][1]:
                    tmp=listIndexDist[i]
                    listIndexDist[i]=listIndexDist[j]
                    listIndexDist[j]=tmp
         
    return [listIndexDist[i] for i in range(k)]

def calcDist(x1,y1,x2,y2):
    return pow(x1-x2,2)+pow(y1-y2,2)

def ex1(Q, file_db, k):
    PointList=[]
    with open(file_db) as F:
        readed=F.readline()
        index=0
        while len(readed)>0:
            PointList.append(readed.strip().split())
            readed=F.readline()
    listIndexDist=[]
    for index in range(len(PointList)):
        x1=PointList[index][0]
        y1=PointList[index][1]
        listIndexDist.append((index,calcDist(int(x1), int(y1), Q[0], Q[1])))
    finalList=[]
    
    finalList=ordInDist(listIndexDist,k)
    #print(finalList)
        
        #listIndexDist.remove(elemToPop)
        
    for i in range(len(finalList)):
        for j in range(len(finalList)):
            if finalList[i]!=finalList[j]:
                if finalList[i][1]==finalList[j][1]:
                    if finalList[i][0]>finalList[j][0]:
                        tmp=finalList[i]
                        finalList[i]=finalList[j]
                        finalList[j]=tmp
    return [i[0] for i in finalList]
# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Esercizio 2: 6+3 punti

Scrivere una funzione che prenda in ingresso due nomi di file 'img_in'
e 'img_out'. 
La funzione (6 punti) deve leggere un'immagine png contenuta nel file 'img_in'
costituita da uno sfondo nero e da diversi pixel colorati e costruire e salvare
in un nuovo file 'img_out' un'immagine delle stesse dimensioni di quella
contenuta in img_in. L'immagine ha al più tre pixel per ogni riga.

La nuova immagine dovrà contenere dei segmenti orizzontali calcolati a partire
dall'immagine contenuta nel file 'img_in' nel seguente modo:
    - per ogni riga contenente esattamente tre pixel, è presente esattamente un
      segmento
    - per ogni riga con meno di tre pixel non c'è alcun segmento né
      pixel ma resta nera.
    - ogni segmento è in corrispondenza dei tre pixel della riga dell'immagine in 'img_in',
      presenti sulla stessa riga (esempio: se sulla riga y, ci sono i punti
                                  x1<x2<x3, il segmento andrà dal punto x1 al
                                  punto x3 e avrà lunghezza x3-x1+1)
    - ogni segmento è del colore dato dalla media dei tre colori di x1, x2, x3
      componente per componente (esempio: se le componenti R di x1, x2 e x3 sono
                                 rispettivamente 11, 22, 66, la componente R
                                 del colore del segmento sarà 33)

Le operazioni sui valori delle componenti vanno arrotondate con la funzione
int.

(+3 punti) La funzione, inoltre, a partire dall'immagine salvata in 'img_out', ritorna il
MASSIMO numero di righe consecutive contenenti un segmento 
(1 se tutte tutte le righe sono separate, 0 se nessuna riga contiene segmenti).

Esempio: ex2('img_1.png', 'img1_out.png') dovrà salvare in 'out21.png' un'immagine
         uguale a quella di 'img1_exp.png' e ritornare il valore 18

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni semplici.
"""

import images
def mediaColori(listaColori):
    lung=len(listaColori)
    R=0
    G=0
    B=0
    for i in listaColori:
        R+=i[0]
        G+=i[1]
        B+=i[2]
    return(int(R/lung),int(G/lung),int(B/lung))

def drawSegment(y,x1,x2,color,matrice):
    while x1<=x2:
        matrice[y][x1]=color
        x1+=1
        

def ex2(img_in, img_out):
    # INSERISCI QUI IL TUO CODICE
    righeCons=0
    maxRigheCons=0
    matrix = images.load(img_in)
    nuovaFoto = [[(0,0,0) for i in range(len(matrix[0]))] for i in range(len(matrix))]
    listaCordinate = [] #questa lista conterrà una tupla avente per ordine : altezza riga, punto 1 segmento, punto 2 segmento,colore
    for i in range(len(matrix)):
        #inizio analisi riga
        altezza=i
        primoPuntoSegmento="notFound"
        secondoPuntoSegmento=0
        colors=[]
        puntiTrovati=0
        for j in range(len(matrix[0])):
            if matrix[i][j]!=(0,0,0):
                
                colors.append(matrix[i][j])
                puntiTrovati+=1
                if primoPuntoSegmento=="notFound":
                    primoPuntoSegmento=j
                if secondoPuntoSegmento==0:
                    secondoPuntoSegmento=j
                else:
                    if j>secondoPuntoSegmento:
                        secondoPuntoSegmento=j
            
        if puntiTrovati>=3:
            righeCons+=1
            listaCordinate.append((altezza,primoPuntoSegmento,secondoPuntoSegmento,mediaColori(colors)))
        else:
            if righeCons>maxRigheCons:
                maxRigheCons=righeCons
            righeCons=0
    for point in listaCordinate:
        drawSegment(point[0],point[1],point[2],point[3],nuovaFoto)
        #print(primoPuntoSegmento,secondoPuntoSegmento)
    images.save(nuovaFoto,img_out)
    return maxRigheCons


# %% ----------------------------------- EX.3 --------------------------------- #

"""
Esercizio 3: 8 punti 
Scrivere una funzione ricorsiva o che fa uso di funzioni ricorsive che
prende in input una stringa che rappresenta il nome di una directory e
un intero k e restituisce un dizionario.

All'interno del dizionario le chiavi sono delle stringhe che rappresentano
i percorsi di alcuni file con estenzione '.txt', relativi alla directory in
input, usando '/' come separatore.
Il valore associato ad una chiave è il numero intero dato dalla somma
di tutte le stringhe numeriche contenute nel file indicato dalla chiave.

ATTENZIONE: devono essere presenti nel dizionario soltanto quei file che
contengono delle stringhe numeriche la cui somma è un valore multiplo
dell'intero k preso in input. Si assume che la somma sia sempre diversa
da zero.

Es: se un file contiene "34 casa c4a 22", la somma delle stringhe numeriche
    in esso contenute è 34+22=56 (infatti c4a *non* è una stringa numerica).
    
Non è consentito utilizzare la funzione os.walk.
Per valutare se una stringa è numerica si può utilizzare il metodo isnumeric

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni semplici.
"""

import os


def fromFileToDict(readedFile,diz,path,k):
    somma=0
    for i in readedFile:
        if i.isdecimal():
            somma+=int(i)
    if somma%k==0:
        diz[path]=somma
            

def recEx3(path,k,diz):
    listaDir=os.listdir(path)
    for i in listaDir:
        if os.path.isdir(path+"/"+i):
            recEx3(path+"/"+i,k,diz)
        else:
            if ".txt" in i:
                with open(path+"/"+i) as F:
                   fromFileToDict(F.read().split(),diz,path+"/"+i,k) 
        
def ex3(path, k):
    diz={}
    # INSERISCI QUI IL TUO CODICE
    recEx3(path,k,diz)
    return diz


# %% ----------------------------------- EX.4 ----------------------------------- #
'''
Esercizio 4: 9 punti (6+3)

L'operazione di accodamento "§" fra due stringhe A e B è possibile se la stringa
A termina con il primo carattere della stringa B. Il risultato dell'operazione
A § B è simile alla concatenazione, soltanto che il primo carattere di B è
rimosso:  dog § good = dogood.

Scrivere una funzione ricorsiva o che fa uso di funzioni ricorsive che
prende in input una stringa start e un set di stringhe words e calcola
ricorsivamente tutte le possibili stringhe massimali che possono essere generate
da accodamenti successivi a partire dalla stringa start, rimuovendo le parole
accodate.

 NOTA: con 'rimovendo le parole accodate' si intende che ogni volta
 che una parola in words è stata concatenata a start con successo,
 l'esplorazione di quel ramo dell'albero di gioco continua senza
 riusare quella parola.  Si veda negli esempi sotto come viene
 aggiornato l'insieme di parole valide per ogni mossa dell'albero
 di gioco.

Per massimale si intende che una stringa non può essere più ulteriormente
concatenata con alcuna altra stringa rimasta in words, dopo tutti gli
accodamenti.

La funzione deve ritornare l'insieme di tutte le stringhe che è possibile
generare (ovvero le foglie dell'albero di gioco), come un insieme (6 punti),
    oppure (+3 punti) come una lista ordinata in in cui:
    - le stringhe sono ordinate in modo crescente rispetto alla loro lunghezza
    - in caso di pari lunghezza, in ordine alfabetico.

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni semplici.

Esempio 1: 'aa' {'abb', 'acc', 'bdd', 'be'}

aa {abb, acc, bdd, be}
|
|- § abb -- aabb {acc, bdd, be}
|  |
|  |- § bdd -- aabbdd(*) {acc, be}
|  |
|  |- § be -- aabbe(*) {acc, bdd}
|
|- § acc -- aacc(*) {abb, bdd, be}

Le stringhe con (*) sono massimali rispetto al set words CORRENTE.

Nell'esempio ex4('aa' ,{'abb', 'acc', 'bdd', 'be'}) la funzione ritorna l'insieme
{'aacc', 'aabbdd', 'aabbe'} (6 punti)
oppure la lista
['aacc', 'aabbe', 'aabbdd'] (9 punti)


Esempio 2: 'dog' {'good', 'gost', 'goat', 'mood', 'doom', 'gasp', 'pool', 'long', 'loud'}

dog {good, gost, goat, mood, doom, gasp, pool, loop}
|
|- § gost -- dogost(*) {good, goat, mood, doom, gasp, pool, loop}
|
|- § goat -- dogoat(*) {good, gost, mood, doom, gasp, pool, loop}
|
|- § good -- dogood {gost, goat, mood, doom, gasp, pool, long, loud}
|  |
|  |- § doom -- dogoodoom {gost, goat, mood, gasp, pool, long, loud}
|     |
|     |- § mood -- dogoodoomood(*) {gost, goat, gasp, pool, long, loud}
|
|- § gasp -- dogasp {good, gost, goat, mood, doom, pool, long, loud}
   |
   |- § pool -- dogaspool {good, gost, goat, mood, doom, long, loud}
      |
      |- § loud  -- dogaspooloud {good, gost, goat, mood, doom, long}
      |  |
      |  |- § doom -- dogaspooloudoom {good, gost, goat, mood, long}
      |     |
      |     |- § mood -- dogaspooloudoomood(*) {good, gost, goat, long}
      |
      |- § long -- dogaspoolong {good, gost, goat, mood, doom, loud}
         |
         |- § good -- dogaspoolongood {mood, gost, goat, doom, loud}
         |  |
         |  |- § doom -- dogaspoolongoodoom {mood, gost, goat, loud}
         |     |
         |     |- § mood -- dogaspoolongoodoomood(*) {gost, goat, loud}
         |
         |- § gost -- dogaspoolongost(*) {good, goat, mood, doom, loud}
         |
         |- § goat -- dogaspoolongoat(*) {good, gost, mood, doom, loud}
         
Le stringhe con (*) sono massimali rispetto al set words CORRENTE 
(non possono essere allungate ulteriormente).

Nell'esempio ex4('dog',  {'good', 'gost', 'goat', 'mood', 'doom', 'gasp', 'pool', 'long', 'loud'})
la funzione ritorna l'insieme
{'dogaspoolongoodoomood', 'dogaspooloudoomood', 'dogoodoomood', 'dogaspoolongost',
 'dogaspoolongoat', 'dogost', 'dogoat'} (6 punti)
oppure la lista
['dogoat', 'dogost', 'dogoodoomood', 'dogaspoolongoat',
'dogaspoolongost', 'dogaspooloudoomood', 'dogaspoolongoodoomood']
 (9 punti)
'''

def concatenate(start,word):
    a=""
    for i in range(len(word)):
        if i!=0:
            a+=word[i]
    return start+a
def rec4ex(start, words,listaMassimali):
    massimale=0
    notFound=True
    for word in words:
        if start[-1]==word[0]:
            notFound=False
            newStart=concatenate(start,word)
            newList=[]
            newList[:]=words
            newList.remove(word)
            rec4ex(newStart, newList,listaMassimali)
        else:
            massimale=start
    if massimale!=0 and notFound:
        listaMassimali.append(massimale)
        
def ex4(start, words):
    listaMassimali=[]
    rec4ex(start, words,listaMassimali)
    
    for i in range(len(listaMassimali)):
        for j in range(len(listaMassimali)):
            if i!=j:
                if len(listaMassimali[i])<len(listaMassimali[j]):
                    tmp=listaMassimali[i]
                    listaMassimali[i]=listaMassimali[j]
                    listaMassimali[j]=tmp
                if len(listaMassimali[i])==len(listaMassimali[j]):
                    a=listaMassimali[i]
                    b=listaMassimali[j]
                    c=min(a,b)
                    if listaMassimali[i]==c:
                        tmp=listaMassimali[i]
                        listaMassimali[i]=listaMassimali[j]
                        listaMassimali[j]=tmp
    print(listaMassimali)
    return listaMassimali
        



###############################################################################
if __name__ == '__main__':
    start = 'aa'
    words = {'abb', 'acc', 'bdd', 'be'}
    expected = ['aacc', 'aabbe', 'aabbdd']
    ex4(start,words)
    # inserisci qui i tuoi test
    
