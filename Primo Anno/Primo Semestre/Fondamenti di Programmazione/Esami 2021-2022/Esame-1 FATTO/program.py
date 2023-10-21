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


# %% ----------------------------------- EX.1 ----------------------------------#
"""
Ex1: 6 punti
Si definisca la funzione ex1(triangles) che prende in input una lista
di triple di numeri positivi ed elimina dalla lista tutte le triple
che non possono essere i lati di un triangolo rettangolo. Ogni numero della
tripla puo' essere o cateto o ipotenusa e non vi è alcun ordine
prestabilito.  La funzione deve ritornare il numero di triple
eliminate dalla lista triangles. La lista triangles deve risultare
modificata in-place alla fine dell'esecuzione di ex1. Per valutare se un
triangolo è rettangolo si può usare il teorema di Pitagora, per cui la
somma dei quadrati costruiti sui cateti deve essere uguale al quadrato
costruito sull'ipotenusa.
Per i confronti, si usi la funzione di arrotondamento round(x,3).

Esempio: se triangles = [(3, 4, 5), (12, 36.05551, 34),
                         (1,1,3), (8,8,8), (2, 3, 4)],
         la funzione ex1(triangles) resituisce il valore 3 e modifica la lista
         in modo che
            triangles = [(3, 4, 5), (12, 36.05551, 34)].

Infatti, considerando il risultato atteso triangles = [(3, 4, 5), (12, 36.05551, 34)]
vale:

| tripla             | check is True                                  |
| (3, 4, 5)          | round( 3² + 4² ), 3) == round( 5² ,3)          |
| (12, 36.05551, 34) | round( 12² + 34² ), 3) == round( 36.05551² ,3) |

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""


def check_valid(a,b,c):
    if (round(a**2+b**2,3)  == round(c**2,3)):
        return True
    if (round(b**2+c**2,3)  == round(a**2,3)):
        return True
    if (round(a**2+c**2,3)  == round(b**2,3)):
        return True
    return False

def ex1(triangles):
    eliminated_triples=0
    newTriples=[]
    # INSERISCI QUI I TUO CODICE
    for triangle in triangles:
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]
        if check_valid(a,b,c):
            newTriples.append(triangle)
        else:
            eliminated_triples+=1
            
    triangles[:]= newTriples   
    return eliminated_triples


# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex2: 8 punti
Si deve costruire un'immagine a partire da un'immagine nera con dei
punti colorati e un dizionario che associa ad alcuni colori una tupla
con esattamente due interi positivi, rappresentanti altezza e
larghezza, rispettivamente.

Si definisca la funzione ex2 che prende in input due stringhe (img_in
e img_out, che rappresentano il nome di due file) e un dizionario
colors.  Il file indicato da img_in contiene un'immagine PNG con
sfondo nero e con alcuni punti colorati. La funzione deve costruire
per ogni punto colorato di img_in un rettangolo in cui il punto è
l'angolo superiore sinistro e le cui dimensioni sono associate al
colore del punto nel dizionario colors. L'immagine con i rettangoli
deve essere salvata in formato PNG in un file con nome img_out.  La
funzione deve ritornare il numero di rettangoli disegnati.

Se il colore di un punto non è presente nel dizionario, quel punto non
dovrà diventare un rettangolo nell'immagine nuova, ma dovrà essere
presente anche nella nuova immagine—–a meno che non è ricoperto da un
altro rettangolo.
ATTENZIONE: si deve disegnare un rettangolo PER OGNI punto di un
colore in colors, ANCHE SE un punto viene coperto da un rettangolo di
un altro punto.  

I rettangoli vanno disegnati nell'ordine dei punti nell'immagine,
considerando ogni punto come una tupla (riga, colonna): ad esempio,
prima il rettangolo per il punto (0,0), seguito da quello per (0,100),
seguito da (30,0).

Si può assumere che le dimensioni in colors richiedono di disegnare
rettangoli con tutti i punti entro i margini dell'immagine (ovvero
i rettangoli non superano mai i margini dell'immagine).

img_in = 'ex2/image01.png'
colors = {(255,0,0):(10,20), (0,255,0):(30,40), (255,0,255):(10,10)}
l'immagine da costruire è quella nel file ex2/expected01.png

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""
import images
def draw_rect_in_position(Matrice,pos,Dimension,color):
   
    TotOg=pos
    xOrigin = pos[0]
    yOrigin = pos[1]
    maxx=pos[0]+Dimension[0]
    while(pos[0]<=maxx-2):
        pos=(pos[0]+1,pos[1])
        Matrice[pos[0]][pos[1]]=color
    pos=(xOrigin,pos[1]+Dimension[1]-1)    
    while(pos[0]<=maxx-2):
        pos=(pos[0]+1,pos[1])
        Matrice[pos[0]][pos[1]]=color 
     
    pos=TotOg
    
    maxx=pos[1]+Dimension[1]
    while(pos[1]<=maxx-2):
        pos=(pos[0],pos[1]+1)
        Matrice[pos[0]][pos[1]]=color 
        
    pos=(pos[0]+Dimension[0]-1,yOrigin)    
    while(pos[1]<=maxx-2):
        pos=(pos[0],pos[1]+1)
        Matrice[pos[0]][pos[1]]=color 
        
        
def ex2(img_in, img_out, colors):
    nrect=0
    newDiz = {}
    Matrice = images.load(img_in)
    for i in range(len(Matrice)):
        for j in range(len(Matrice[0])):
            for k in colors.keys():
                if k == Matrice[i][j]:
                    newDiz[k]=(i,j,colors[k])
   
    for positions in newDiz:
        pos = (newDiz[positions][0],newDiz[positions][1])
        for i in range(len(Matrice)):
            for j in range(len(Matrice[0])):
                if pos==(i,j):
                    nrect+=1
                    draw_rect_in_position(Matrice,pos,newDiz[positions][2],positions)
    images.save(Matrice,img_out)  
    return nrect     

    
# %% ----------------------------------- EX.3 ----------------------------------- #
"""
Ex3: 9 punti
Si definisca la funzione ricorsiva ex3 che prende una stringa
directory e una stringa namefile. La funzione deve cercare
ricorsivamente all'interno della directory indicata da directory e in
tutte le sotto-directory i file con nome uguale a namefile.  Tali file
vanno interpretati come file di testo che contengono soltanto stringhe
numeriche positive. I file con lo stesso namefile hanno sempre lo
stesso numero di stringhe numeriche.  La funzione deve ritornare una
lista di interi ottenuta sommando le stringhe numeriche dei file
individuati, posizione per posizione.

Esempio: se vengono trovati soltanto due file di nome namefile e tali
file contenengono le sequenze "11 23 90" e "11 77 0", la funzione ex3
ritorna la lista [22, 100, 90].

Si suggerisce di usare le funzioni os.listdir, os.path.isfile e
os.path.isdir.  e di NON usare la funzione os.join in Windows (usare
la concatenazione fra stringhe con il carattere '/')

È proibito usare la funzione os.walk

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""

import os

def readAndUpdate(directory,i,finalList):
    with open(directory+"/"+i) as f:
        file=str(f.read()).split()
        for j in range(len(file)):
            if len(finalList)<j+1:
                finalList.append(0)
                finalList[j]+=int(file[j])
            else:
                finalList[j]+=int(file[j])
def search(directory,finalList,namefile):
    listaDir=os.listdir(directory)
    for i in listaDir:
        if ".txt" not in i:
            search(directory+"/"+i,finalList,namefile)  
        else:
            if namefile in i:
                readAndUpdate(directory,i,finalList)      
    return finalList                
def ex1(directory, namefile):
    finalList=[]
    search(directory,finalList,namefile)
    return finalList

    
# %% ----------------------------------- EX.4 ----------------------------------- #
"""
Ex4: 6+3 punti
Si definisca una funzione ricorsiva (o che usa funzioni ricorsive)
ex4(strings, n) che prende un insieme strings di stringhe e un intero
n e genera ricorsivamente tutte le possibili stringhe che possono
essere costruite concatenando n stringhe di strings.  La funzione deve
ritornare tutte le stringhe costruite. La funzione può restituire o un
insieme con tutte le stringhe create (6 punti), oppure una lista
ordinata (9 punti).
La lista è ordinata consideranto l'ordine decrescente della lunghezza
delle stringhe e, in caso di parità, l'ordine alfabetico.

Esempio: se strings={'a','b','c','de'}, la funzione ex4(strings, 2)
ritorna l'insieme {'ab','ac','ade','ba','ca','dea','bc','bde','cb','deb','cde','dec'} (6 punti)
oppure la lista ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'] (9 punti)
"""
def ex4(strings, n):
    def concatenating(letter,lista,n,finalList):
        if n==0:
            return False
        if n==1:
            concatenating(letter,lista,n-1,finalList)  
            for j in lista:
                finalList.append(letter+j)
        else:
            for j in lista:
                tmp = lista.copy()
                tmp.remove(j)
                concatenating(letter+j,tmp,n-1,finalList)  
    def sorting(finalList):
        for i in range(len(finalList)):
            for j in range(len(finalList)):
                if i != j:
                    if len(finalList[i])>len(finalList[j]):
                        tmp = finalList[i]
                        finalList[i]=finalList[j]
                        finalList[j]=tmp
                    if len(finalList[i])==len(finalList[j]):
                        tmp=max(finalList[i],finalList[j])
                        if finalList[i]!=tmp:
                            tmp2 = finalList[i]
                            finalList[i]=finalList[j]
                            finalList[j]=tmp2
    def ex2(strings, n):
        # WRITE HERE YOUR CODE
        finalList=[]
        for i in strings:
            tmp = strings.copy()
            tmp.remove(i)
            concatenating(i,tmp,n-1,finalList)
        sorting(finalList)
        return finalList
###################################################################################
if __name__ == '__main__':
    
    # inserisci qui i tuoi test
    #print(ex3('/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Esami/2021-2022/esame-12-9-22-sol/ex3/A','a.txt'))
    #print(ex2('/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Esami/2021-2022/Esame-1/ex2/image01.png',
    #           '/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Esami/2021-2022/Esame-1/ex2/expected01.png',
    #           {(255,0,0):(10,20), (0,255,0):(30,40), (255,0,255):(10,10)}))
    print('Ciao')