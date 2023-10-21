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

import os
from tree import BinaryTree
nome = "Marco"
cognome = "Casu"
matricola = "2046212"

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

""" Es 1: 6 punti

Parte 1)
E' dato in ingresso un dizionario D che ha come chiave un intero
e come valore una lista di interi con ripetizioni.

D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}

Si implementi la funzione ex1(D, list_rm) che restituisca il dizionario
"inverso" W in cui:
 - esiste una chiave per ogni intero presente nelle liste dei valori di D
 - i nuovi valori di W sono le chiavi di D che hanno generato la
   chiave di W, ripetute per quante volte la chiave di W è presente nel
   valore delle chiavi di D.

Il dizionario inverso W deve avere ciascuna lista associata alla
chiave, ordinata in modo che prima vi siano i numeri pari e poi i
dispari; a sua volta i pari sono ordinati in maniera decrescente e i
dispari in maniera crescente.

L'esempio sopra deve restituire:

    W = {6: [2], 4: [2, 1, 1, 1], 2: [1], 3: [2, 1], 5: [2]}

Parte 2) Si estenda la funzione ex1(D, list_rm) in modo che siano
cancellati dal dizionario D in maniera distruttiva tutti gli interi nei
valori di D che compaiono in list_rm. Se dopo aver rimosso i valori una
lista in D è vuota, allora la chiave corrispondente deve essere cancellata
dal dizionario.

Esempio: se D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}
         e list_rm = [4, 3, 2, 5]
         D deve essere trasformato in maniera distruttiva in
         {2: [6]} in quanto sono tolti tutti i valori tranne il 6
         e D non contiene più la lista vuota associata alla chiave 1.
"""


def ex1(D, list_rm):
    # INSERISCI IL TUO CODICE QUI
    W = {}
    for i in D:
        lista = D[i]
        for j in lista:
            if j not in W:
                W[j] = [i]
            else:
                W[j].append(i)
    for i in W:
        W[i].sort(reverse=True)

    W = list(W.items())
    for i in range(len(W)):
        for j in range(len(W)):
            if W[i]!=W[j]:
                if W[i][0]%2==0:
                    if W[j][0]%2!=0:
                        tmp=W[i]
                        W[i]=W[j]
                        W[j]=tmp
                
                
    #print(W)        
            
    for i in range(len(W)):
        if W[i][0]%2==0:
            for j in range(len(W)):
                if W[j][0]%2==0:
                    if W[i]>W[j]:
                        tmp=W[i]
                        W[i]=W[j]
                        W[j]=tmp
                
                        
    for i in range(len(W)):
        if W[i][0]%2!=0:
            for j in range(len(W)):
                if W[j][0]%2!=0:
                    if W[i]<W[j]:
                        tmp=W[i]
                        W[i]=W[j]
                        W[j]=tmp
    for key in D:
        lista=D[key]
        nuovaLista=[]
        for i in lista:
            if i not in list_rm:
                nuovaLista.append(i)
        D[key]=nuovaLista
    keyToRemove=[]
    for key in D:
        if len(D[key])<=0:
            keyToRemove.append(key)
    for i in keyToRemove:
        D.pop(i)
    print(W)
    for key in W:
       
        for i in range(len(key[1])):
            for j in range(len(key[1])):
                if i!=j:
                    if key[1][i]%2==0:
                        if key[1][j]%2!=0:
                            tmp=key[1][i]
                            key[1][i]=key[1][j]
                            key[1][j]=tmp
            
    for key in W:
        for i in range(len(key[1])):
            for j in range(len(key[1])):
                if i!=j and key[1][i]%2==0 and  key[1][j]%2==0:
                    if key[1][i]>key[1][j]:
                            tmp=key[1][i]
                            key[1][i]=key[1][j]
                            key[1][j]=tmp
    for key in W:
        for i in range(len(key[1])):
            for j in range(len(key[1])):
                if i!=j and key[1][i]%2!=0 and  key[1][j]%2!=0:
                    if key[1][i]<key[1][j]:
                            tmp=key[1][i]
                            key[1][i]=key[1][j]
                            key[1][j]=tmp
    print(W)
    return dict(W)


# ----------------------------------- EX.2 ----------------------------------- #

''' Ex 2: 8 punti
    Si implementi una funzione che prende in ingresso una stringa di
    caratteri 'path' e una lista di liste 'griglia' e restituisca una
    lista. La stringa rappresenta una sequenza di spostamenti da
    effettuare sulla griglia, immaginando di partire dall'elemento in
    alto a sinistra (0,0). Gli spostamenti possibili sono 'R' (destra/right),
    'L' (sinistra/left), 'U' (su/up), 'D' (giù/down) o 'S' (pausa/stay).
    La funzione restituisce la lista dei valori incontrati sulla griglia
    seguendo la sequenza di spostamenti 'path'.
    Se la sequenza prevede uno spostamento al di fuori della griglia, il
    valore da inserire si immagina essere quello che si incontra
    rientrando nella griglia dal punto opposto.
    Se la sequenza prevede un carattere diverso dagli spostamenti elencati,
    allora la lista deve interrompersi all'ultimo valore della sequenza
    prima della mossa non valida.

    Es:
        Immaginando che la griglia è la seguente:
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 1, 2]]
        Se la sequenza è 'RRDS',   la lista restituita sarà [2,3,7,7],
        Se la sequenza è 'RRUSRR', la lista restituita sarà [2,3,1,1,2,9],
        Se la sequenza è 'DDXUU',  la lista restituita sarà [5, 9].
'''
def calcNextStep(pos,mov,limitY,limitX):
    y=pos[0]+mov[0]
    x=pos[1]+mov[1]
    return (y%limitY,x%limitX)

def ex2(griglia, path):
    listaValori=[]
    limitY=len(griglia)
    limitX=len(griglia[0])
    pos=(0,0)
    dizMovement={'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
    for command in path:
        if command!="S":
            pos = calcNextStep(pos,dizMovement[command],limitY,limitX)
        print(pos)
        for i in range(len(griglia)):
            for j in range(len(griglia[0])):
                if (i,j)==pos:
                    listaValori.append(griglia[i][j])
    return listaValori

# ----------------------------------- EX.3 ----------------------------------- #


''' Ex 3: 9 punti
    Si implementi una funzione ricorsiva che prende in ingresso la
    radice di un albero e un intero. L'albero è realizzato attraverso
    istanze della classe BinaryTree definita nel file tree.py.
    La funzione ritorna il prodotto delle somme di tutte i nodi che sono
    un figlio sinistro per le somme di tutti i nodi che sono figlio destro
    a una profondità pari all'intero depth ricevuto in input.
    Si assume che la radice è a profondità 0.

    Es:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    Se l'albero è quello di sinistra e p=2, la funzione ritorna il valore
    9*(1+3)=36.
    Se l'albero è quello di destra e p=3, la funzione ritorna il valore
    (2+8+2)*(-1+1+3+9)=144.
    '''

def rec3(actualDepth,root,listValue,depth,sxORdx):
    #print(actualDepth)
    if actualDepth!=depth:
        if root.sx!=None:
            rec3(actualDepth+1,root.sx,listValue,depth,0)
        if root.dx!=None:
            rec3(actualDepth+1,root.dx,listValue,depth,1)
    else:
        listValue[sxORdx]+=root.valore


def ex3(root, depth):
    listValue=[0,0]
    actualDepth=0
    rec3(actualDepth,root,listValue,depth,0)
    return listValue[0]*listValue[1]
    ### INSERIRE QUI IL CODICE ###


# ----------------------------------- EX.4 ----------------------------------- #

''' Ex 4: 9 punti
    Si implementi una funzione ricorsiva o che usa funzioni/metodi ricorsivi
    che prende in ingresso due percorsi (dirin e dirout) e un intero 'depth'
    e crea all'interno della directory 'dirout' un file per ogni file di testo (.txt)
    raggiungibile dal percorso 'dirin' percorrendo esattamente 'depth' sottodirectory.
    La struttura di sottodirectory che contengono il file deve essere ricreata
    sotto dirout.

    Ogni file da creare all'interno dei 'dirout' avrà lo stesso contenuto
    del file originario, ma con il minuscolo/maiuscolo invertito (ovvero
    ogni lettera minuscola sarà presente come maiuscola e viceversa).
    I caratteri non alfabetici vanno mantenuti tal quali.
    La funzione ritorna il numero totale di byte scritti all'interno
    dei file creati in 'dirout'. Si assuma che tutti i nomi di file
    raggiungibili nelle sottodirectory di 'dirin' siano univoci.

    NOTA: possono esservi utili le funzioni: os.listdir, os.path.join,
    os.path.isfile, os.mkdir, os.path.exists ...
    NOTA: è proibito usare la funzione os.walk

'''
def RevUpperString(stringa,byteScritti):
    newStringa=""
    for i in stringa:
        byteScritti[0]+=len(i)
        if i.isalpha():
            if i.islower():
                newStringa+=i.upper()
            else:
                newStringa+=i.lower()
        else:
            newStringa+=i
    return newStringa

def extractStringFromFile(path):
    with open(path) as f:
        return f.read()
    
def scriviFileDaLista(lista,stringa,ogLista,percorso):
    if len(lista)>1:
        if percorso!="":
            if lista[0] not in os.listdir(percorso):
                    os.mkdir(percorso+lista[0])
        else:
            if lista[0] not in os.listdir():
                    os.mkdir(percorso+lista[0])
                
        percorso+=lista[0]+"/"
        lista.pop(0)
        scriviFileDaLista(lista,stringa,ogLista,percorso)
    else:
        s=""
        for i in ogLista:
            if i!=ogLista[-1]:
                s+=i+"/"
            else:
                s+=i
        with open(s,"w") as F:
            F.write(stringa)
        
        
def rec4(dirin,MaxDepth,actualDepth,percorso,byteScritti,dirout):
    directoryFiglie=os.listdir(dirin)
    for elem in directoryFiglie:
        if os.path.isdir(dirin+"/"+elem):
            rec4(dirin+"/"+elem,MaxDepth,actualDepth+1,percorso+"/"+elem,byteScritti,dirout)
        else:
            if ".txt" in elem and actualDepth==MaxDepth:
                X=percorso.split("/")
                X.append(elem)
                pathWrite=[dirout]
                X.pop(0)
                pathWrite+=X
                stringaDaScrivere=RevUpperString(extractStringFromFile(dirin+"/"+elem),byteScritti)
                scriviFileDaLista(pathWrite,stringaDaScrivere,pathWrite.copy(),"")
def ex4(dirin, dirout, depth):
    byteScritti=[0]
    rec4(dirin,depth,0,"",byteScritti,dirout)
    return byteScritti[0]
    
    ### INSERIRE QUI IL CODICE ###

# --------------------------------------------------------------------------- #

import tree
if __name__ == '__main__':
   D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}
   D_rm = {2: [6]}
   to_remove = [4, 3, 2, 5]
   ex1(D,to_remove)
    ### INSERIRE QUI I VOSTRI TEST ###
