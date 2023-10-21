#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA
 3) Rinominare la directory examPY con il proprio numero di matricola
"""
nome        = "MARCO"
cognome     = "CASU"
matricola   = "2046212"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla fine di grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################
# ----------------------------------- EX.1 ----------------------------------- #
''' Ex 1: 7 punti
    Si implementi una funzione che prende in ingresso tre nomi di file
    e restituisce una coppia di numeri interi.
    I parametri file1 e file2 sono stringhe contenenti i nomi di due file
    di testo. Questi file contengono, su ogni riga, una serie di stringhe
    separate da spazi, tabulazioni, virgole o punti e virgola.
    La funzione deve scrivere all'interno di un nuovo file indicato da
    file3 una riga per ogni riga di file1 la cui corrispondente riga in
    file2 ha almeno una stringa in comune. In particolare:
        - date le stringhe della riga i-esima di file1, se la riga i-esima
          di file2 contiene almeno una di tali stringhe, allora in file3
          sarà presente una riga con tutte le stringhe in comune.
        - Le stringhe in comune sono scritte nelle righe di file3 separate
          da uno spazio e ordinate per numero di caratteri crescente e, in
          caso di parità, in ordine alfabetico.
        - Le righe in file3 hanno lo stesso ordine delle righe di origine.
    La funzione ritorna una tupla in cui il primo e il secondo elemento
    sono, rispettivamente, il numero di stringhe e il numero di righe
    scritte in file3.
'''

def clearStringInList(lista):
    for strings in range(len(lista)):
        for value in range(len(lista[strings])):
            lista[strings][value]=lista[strings][value].replace(","," ").replace(";"," ").strip()
            #print(lista[strings][value])
    for strings in range(len(lista)):
        for value in range(len(lista[strings])):
            if " " in lista[strings][value]:
                nuoviValori=lista[strings][value].split()
                lista[strings].remove(lista[strings][value])
                for i in nuoviValori:
                    lista[strings].append(i)
    return lista
    
                
    
    
def getListFromFile(file):
    
    listaRighePrimoFile=[]
    with open(file) as F:
        while True:
            readedLine=F.readline()
            if len(readedLine)<=0:
                break
            listaRighePrimoFile.append(readedLine.split())
    return listaRighePrimoFile

def ex1(file1, file2, file3):
    stringheScritte=0
    righeScritte=0
    lista1=clearStringInList(getListFromFile(file1))
    lista2=clearStringInList(getListFromFile(file2))
    lista3=[]
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            tmp=[]
            if i==j:
                for stringaLista1 in range(len(lista1[i])):
                    if lista1[i][stringaLista1] in lista2[j]:
                        tmp.append(lista1[i][stringaLista1])
            if len(tmp)>=1:
                lista3.append(tmp)
    for i in range(len(lista3)):
        a = sorted([x for x in lista3[i]],key = lambda x : (len(x),x))
        lista3[i][:]=a
    with open(file3,"w") as F:
        for i in lista3:
            righeScritte+=1
            for j in i:
                F.write(j)
                stringheScritte+=1
                if j!=i[-1]:
                    F.write(" ")
            F.write("\n")
    return(stringheScritte,righeScritte)
# ----------------------------------- EX.2 ----------------------------------- #
''' Ex. 2: 7 punti
    Si scriva una funzione ex2(gridFilePath) che, data una griglia NxN
    contenuta in un file json come una lista di liste, restituisce un
    intero positivo. Nella griglia fornita come input, ogni cella può
    avere uno dei tre valori seguenti:
       - il valore 0 rappresenta una cella vuota;
       - il valore 1 rappresenta un'arancia matura;
       - il valore 2 rappresenta un'arancia marcita.
    Ogni minuto, una qualsiasi arancia matura che è adiacente
    orizzontalmente o verticalmente ad una arancia marcita diventa
    anch'essa marcia.

    La funzione deve restituire il minimo numero di minuti che
    possono trascorrere fino a quando nessuna cella contiene più
    un'arancia matura. Se questo è impossibile, deve restituire -1.

    Ad esempio, data la griglia:
    [[2,1,1],
     [1,1,0],
     [0,1,1]]
    la funzione deve restituire 4.

    Mentre, data la griglia:
    [[2,1,1],
     [0,1,1],
     [1,0,1]]
    la funzione rende -1.

    Nota: per caricare la griglia potete usare json.load()

'''


def contaminate(griglia,pos,actPos):
    canCon=False
    for i in pos:
       if i[0]>=0 and i[0]<len(griglia) and i[1]>=0 and i[1]<len(griglia[0]):
           if griglia[i[0]][i[1]]==1:
               griglia[i[0]][i[1]]=2
               canCon=True
    return canCon    

import json
def ex2(gridFilePath):
    
    griglia2=[]
    with open(gridFilePath) as F:
        griglia=F.read()
    
    tmp=[]
    for i in griglia:
        if i.isdigit():
            tmp.append(int(i))
        if i=="]":
            griglia2.append(tmp)
            tmp=[]
    griglia2.pop(-1)
    
    minutePassed=0
    for i in range(len(griglia2)):
        for j in range(len(griglia2[0])):
            if griglia2[i][j]==2:
                if contaminate(griglia2,[(i,j+1),(i,j-1),(i+1,j),(i-1,j)],(i,j)):
                
                    minutePassed+=1
                    
    for i in range(len(griglia2)):
        for j in range(len(griglia2[0])):
            if griglia2[i][j]==1:
                return -1
    #print(griglia2)
    return minutePassed
    
            
# ----------------------------------- EX.3 ----------------------------------- #
''' Ex 3: 9 punti
    Si implementi una funzione ricorsiva che prende in ingresso una
    coppia di stringhe a e b, e un intero k e ritorna una lista.
    Nella lista sono contenute tutte le possibili stringhe che si
    possono ottenere dalla concatenazione di una sottostringa di
    lunghezza k della prima stringa con una sottostringa di lunghezza
    k della seconda stringa.  La lista ritornata è ordinata in ordine
    rispetto alla posizione della sottostringa di a in a e, a
    parimerito, in ordine della sottostringa di b in b.

    esempio: ex3('casa', 'riccio', 3) ritorna la lista:

     ['casric', 'casicc', 'cascci', 'cascio', 'asaric', 'asaicc',
     'asacci', 'asacio']

    AVVISO: non inserite la vostra funzione ricorsiva dentro un'altra
    funzione, altrimenti il sistema di test non la rileverà la ricorsione
    e tutti i test falliranno.
'''

def concatenate(sA,lista,listaFinale):
    if sA==0:
        return
    if len(lista)!=1:
        for sB in lista:
            listaFinale.append(sA+sB)
            concatenate(0,lista,listaFinale)   
    else:
        pass
def concatenate2(sA,sB,listaFinale):
    if len(sA)>0:
        for i in sB:
            listaFinale.append(sA[0]+i)
        sA.pop(0)   
        concatenate2(sA,sB,listaFinale)
        
def ex3(a, b, k):
    SottostringheA=[a[i:k+i] for i in range(len(a))  if len(a[i:k+i])==k]
    SottostringheB=[b[i:k+i] for i in range(len(b))  if len(b[i:k+i])==k]
    listaFinale=[]
    #for i in SottostringheA:
    concatenate2(SottostringheA,SottostringheB,listaFinale)
    return listaFinale


# ----------------------------------- EX.4 ----------------------------------- #
'''Ex. 4: 9 punti
    Scrivere una funzione ex4(folderPath), ricorsiva o utilizzando
    funzioni/metodi ricorsivi che, dato il percorso di una cartella
    che è la radice di un albero di cartelle contenente solo file di
    testo, crea e restituisce un dizionario in cui:

     - c'è una coppia (chiave, valore) per ogni file di testo che è
       stato trovato nella cartella folderPath o, ricorsivamente, in
       una qualsiasi delle sue sottocartelle;
     - ogni chiave è il percorso di un file di testo, relativo alla
       cartella folderPath radice della prima chiamata a ex4;
     - il valore corrispondente è un intero, ottenuto come somma
       dei valori unicode di tutti i caratteri del file di testo,
       SENZA includere i caratteri di accapo.

    Per esempio, dato il seguente albero di cartelle:

    ex4/test01/
        |-f1
            |-f1-1

    e i seguenti file:

    ex4/t1.txt - contenuto del file: hello world
    ex4/f1/f1-1/t2.txt - contenuto del file: let's count to 3, 1-2-3

    ex4("ex4") restituirà il dizionario
    {'ex4/t1.txt': 1116, 'ex4/f1/f1-1/t2.txt': 1722}
    poiché la somma dei valori unicode di "hello world" è 1116,
    mentre quella di "let's count to 3, 1-2-3" è 1722.

    AVVISO: è vietato usare la funzione os.walk.
    AVVISO: non inserite la vostra funzione ricorsiva dentro un'altra
    funzione, altrimenti il sistema di test non la rileverà la ricorsione
    e tutti i test falliranno.
'''

import os

def get_unicode_value(file):
    v=0
    
    with open(file,encoding="utf8") as F:
        a=F.read()
        for i in a:
            if i!="" and i!="\n":
                v+=ord(i)
    return v


def rec4(folder,diz):
    for i in os.listdir(folder):
        if os.path.isdir(folder+"/"+i):
            rec4(folder+"/"+i,diz)
        else:
            diz[folder+"/"+i]=get_unicode_value(folder+"/"+i)
def ex4(folderPath):
    #print(folderPath)
    diz={}
    rec4(folderPath,diz)
    return diz
# ----------------------------------- END ----------------------------------- #
if __name__ == '__main__':
    path =  'ex4/test02'
    expected = {'ex4/test02/f1/f1-1/t1.txt': 42248, 'ex4/test02/f1/f1-2/t2.txt': 83019, 'ex4/test02/f2/f2-1/t1.txt': 1289763, 'ex4/test02/f2/f2-2/t2.txt': 3901860}
    expected = {'ex4/test02/f1/f1-1/t1.txt': 42248, 'ex4/test02/f1/f1-2/t2.txt': 83019, 'ex4/test02/f2/f2-1/t1.txt': 1289763, 'ex4/test02/f2/f2-2/t2.txt': 3901830}
    print(ex4(path))