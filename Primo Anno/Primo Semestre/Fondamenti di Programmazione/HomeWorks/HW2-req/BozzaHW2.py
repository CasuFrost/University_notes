# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:20:01 2022

@author: mcasu
"""

def ValoreAssoluto(value):
 
   if(value<0): 
      return -value
   return value



def decode_value(xkcd : str ) -> int:
    listaInteri = []
    TenXmultiplayer=1
    for i in range(len(xkcd)-1,-1,-1):
        if int(xkcd[i])!=0:
            listaInteri.append(int(xkcd[i])*TenXmultiplayer)    
            TenXmultiplayer=1
        else:
            TenXmultiplayer=TenXmultiplayer*10
            

    for i in range(len(listaInteri)):  
        if i!=0:    
            if listaInteri[i]<ValoreAssoluto(listaInteri[i-1]) :           
                listaInteri[i]*=-1

    return sum(listaInteri)
        

def decode_XKCD_tuple(xkcd_values : tuple[str, ...], k : int) -> list[int]:
    '''
    Riceve una lista di stringhe che rappresentano numeri nel formato XKCD
    ed un intero k positivo.
    Decodifica i numeri forniti e ne ritorna i k maggiori.

    Parameters
    valori_xkcd : list[str]     lista di stringhe in formato XKCD
    k : int                     numero di valori da tornare
    Returns
    list[int]                   i k massimi valori ottenuti in ordine decrescente
    '''
    listaInteri = [decode_value(x) for x in xkcd_values]
    
    
    for i in range(len(listaInteri)):
        for j in range(i,len(listaInteri)):
            if listaInteri[i]>listaInteri[j]:
                listaInteri[i],listaInteri[j] = listaInteri[j],listaInteri[i]
    
    return [listaInteri[i] for i in range(len(listaInteri)-1,(len(listaInteri)-1)-k,-1)]
    #return [newList[i] for i in range(len(newList)-1,(len(newList)-1)-k,-1)]
    
    
def xkcd_to_list_of_weights(xkcd : str) -> list[int]:
    '''
    Spezza una stringa in codifica XKCD nella corrispondente
    lista di interi, ciascuno corrispondente al peso di una lettera romana

    Parameters
    xkcd : str              stringa nel formato XKCD
    Returns
    list[int]               lista di 'pesi' corrispondenti alle lettere romane

    Esempio: '10010010010100511' -> [100, 100, 100, 10, 100, 5, 1, 1,]
    '''
    listaInteri = []
    TenXmultiplayer=1
    for i in range(len(xkcd)-1,-1,-1):
        if int(xkcd[i])!=0:
            listaInteri.append(int(xkcd[i])*TenXmultiplayer)
            
            TenXmultiplayer=1
        else:
            TenXmultiplayer=TenXmultiplayer*10

    return list(reversed(listaInteri))
def list_of_weights_to_number(weigths : list[int] ) -> int:
    '''
    Trasforma una lista di 'pesi' nel corrispondente valore arabo
    tenendo conto della regola di sottrazione

    Parameters
    lista_valori : list[int]    lista di 'pesi' di lettere romane
    Returns
    int                         numero arabo risultante
    
    Esempio: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397
    '''
    weigths = list(reversed(weigths))
    for i in range(len(weigths)):  
        if i!=0:    
            if weigths[i]<ValoreAssoluto(weigths[i-1]) :           
                weigths[i]*=-1

    return sum(weigths)
print(list_of_weights_to_number([1, 10, 100, 1000]))
#print(decode_XKCD_tuple( [ "150",  "1050110" , "100100010100110", "11000", "1500", "10050010100110"],6),"EXPECTED:",[999, 999, 499, 499, 49, 49,])

