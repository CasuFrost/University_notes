# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:14:28 2022

@author: User
"""

def isAnagramma(testo : str, testo1 : str) -> bool :
    #si può definire una funzione all'interno di un altra funzione, ed essa può essere usata solo 
    #al suo interno, inoltre ha accesso alle variabili della funione padre
    def conta_lettere(stringa : str)-> dict[str,int]:
            frequenze = {}
            for c in stringa:
                if c in frequenze :
                    frequenze[c] += 1
                else:
                    frequenze[c] = 1
            return frequenze
    frequenze1 = conta_lettere(testo)
    frequenze2 = conta_lettere(testo1)
    return frequenze1 == frequenze2

print(isAnagramma("onepaper", "onepapre"))
#Standardizzare le parole mettendole in forma canonica,
#Ordiniamole per ordine alfabetico

def isAnagramma2(testo : str, testo1 : str) -> bool :
    # la funzione sorted su una stringa, la trasforma in una lista ordinata alfabeticamente
    #composta dai caratteri della parola
    ordinata1 = sorted(testo)
    ordinata2 = sorted(testo1)
    return ordinata1 == ordinata2

print(isAnagramma2("testo", "otset"))



Scheda = dict[str,str]
Agenda = list[Scheda]

agenda : Agenda = [
    {'nome' : 'paperino','cognome':'Paolino'},
    {'nome' : 'luca','cognome':'coito'},
    {'nome' : 'carlo','cognome':'sborra'},
    {'nome' : 'lava','cognome':'gina'},
    ]



def cerca_lineare(ag : Agenda, colonna : str, valore:str):
    for record in ag:
        if corrisponde_alla_query(record,colonna,valore):
            return record
    return None

def corrisponde_alla_query(riga : Scheda, colonna : str, valore:str)->bool:
    return colonna in riga and riga[colonna] == valore

def cerca_multicolonna_lineare(ag : Agenda, query : Scheda) -> bool:
    trovati = []
    for record in ag:
        if corrispode_alla_query_multicolonna(record,query):
            trovati.append(record)
    return trovati

def corrispode_alla_query_multicolonna(record : Scheda, query : Scheda)-> bool:
    for colonna,cercato in query.items():
        if (colonna not in record or record[colonna] != cercato):
            return False
    
#Stile di programmazione funzionale 
#all : torna True se tutti i valori sono True
#any : torna True se almeno un valore è True

def corrisponde_alla_query_FUN(record : Scheda,query:Scheda):
    return all(chiave in record and record[chiave] == valore for chiave, valore in query.items())
        


def corrisponde_alla_query_SET(record : Scheda,query:Scheda):
    set_query = set(query.items())
    set_record = set(record.items())
    return set_query - set_record == set()
    
def cerca_multicolonna_lineare_LC(ag : Agenda,query:Scheda):
    return [record for record in ag if corrisponde_alla_query_SET(record, query)]






