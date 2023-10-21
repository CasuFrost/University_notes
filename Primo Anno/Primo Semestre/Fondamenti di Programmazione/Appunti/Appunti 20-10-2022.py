# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:23:30 2022

@author: User
"""



#scriviamo un programma che ordini per numero di lettere una lista di stringhe
lista = ["uno","due","tre","quattro","cinque","sei"]
listaPos = []
for i,elemento in enumerate(lista):
    listaPos.append((len(elemento),elemento,i))
    

#lambda si usa per definire una funzione usa e getta 
transforma_elemento = lambda parola : (len(parola),parola)

listaOrdinata = sorted(listaPos,key=lambda parola : (len(parola),parola))
print(listaOrdinata)

#Adesso ordiniamole al contrario, basta cambiare il segno all'ordinamento numerico

listaPos.clear()
listaOrdinata.clear()
for i,elemento in enumerate(lista):
    listaPos.append((len(elemento)*-1,elemento,i))
    

#lambda si usa per definire una funzione usa e getta 
transforma_elemento = lambda parola : (len(parola),parola)

listaOrdinata = sorted(listaPos,key=lambda parola : (len(parola),parola))
print(listaOrdinata)

#List comprension
lista = [1,2,3,4]
listaNuova = [ X**3 for X in lista] #Tale scrittura crea una lista per ogni elemento X nella 
#lista chiamata, operato per la funzione subito dopo le parentesi quadre
print(listaNuova)

#se invece separo 2 valori con 2 punti, posso costruire un dizionario con i valori chiamati,
#per esempio costruiamo ora un dizionario con la chiave il valore originale ed il valore il numero 
#originale alla potenza di 3
lista = [1,2,3,4]
Dizionario = { X:X**3 for X in lista} #si utilizzino le parentesi graffe per i dizionari
print(Dizionario)

#Si può utilizzare anche una condizione, facciamo finta di voler solamente i numeri dispari
lista = [1,2,3,4]
Dizionario = { X:X**3 for X in lista if X%2} #si utilizzino le parentesi graffe per i dizionari
print(Dizionario)

# facciamo finta di voler solamente i numeri pari
lista = [1,2,3,4]
Dizionario = { X:X**3 for X in lista if X%2==0} #si utilizzino le parentesi graffe per i dizionari
print(Dizionario)



#il comando assert fa una verifica, se vero continua con il codice, se falso lancia un messaggio di errore
assert 1>0,"errore"
#si scrive assert, poi la condizione, e poi dopo la virgola la stringa con il messaggio di errore

