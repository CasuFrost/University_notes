def separator():
    print("\n---------Nuova sezione---------\n")



"""
I file sono blocchi di bytes memorizzati nel filesystem
Sono organizzati in una struttura di directory ad albero
SINTASSI per leggere un file bisogna importare la libreria os ed utilizzare la funzione open
essa prende come parametro il filename, la modalità di apertura e l'encoding e ritorna un FILE
"""
import os

"""
se nel filename non è indicato il percorso, il file verrà cercato nella directory in cui è 
presente lo script dalla quale è richiamata
"""

#Esempi
filename = "paperino.txt"
filename = "user/bin/python/paperino.txt"

"""
un file può essere aperto in varie modalità:
    r (read) solo per leggerne il contenuto 
    w (write) per scriverne il contenuto
    a (append) per aggiungere nuovo contenuto alla fine del file

Come seconda lettera si usa t per intendere che si sta leggendo un file di testo.
    Se si omette l'encoding del file, di default leggerà un file di testo 

codifiche :
    ufta
    latin
    ascii
"""

a = open("C:/Nuova cartella/prova.txt",encoding = 'utf8',mode="w")
a.write("Testo scritto su file")
a.close()


#Aprendo un blocco di codice con with fa si che il file alla fine del blocco venga sempre chiuso
with open("C:/Nuova cartella/prova.txt",encoding = 'utf8',mode="a") as a:
    a.write("\ndaje")
    
"""
il comando seek ci permette di spostarci all'interno del file
"""
with open("C:/Nuova cartella/prova.txt",encoding = 'utf8',mode="r") as a:
    print(a.read()) #Leggo il contenuto del file
    a.seek(0) #Così si ritorna all'inizio del file
    print(a.read()) #Dall'inizio rileggo il contenuto del file
    a.seek(0)
    
    separator()
    
    #la funzione read() legge tutto il file
    f = a.read()
    print(f)
    a.seek(0)
    #readline() legge finchè non si va a capo, quindi legge una riga
    f = a.readline()
    print(f)
    a.seek(0)
    #se si passa un intero a read(), leggerà quel numero di caratteri
    f = a.read(5)
    print(f)
    a.seek(0)
    separator()


with open("C:/Nuova cartella/prova.txt",encoding = 'utf8',mode="r") as a:
    
    """
    Un file viene letto come fosse un contenitore di righe, per questo si può
    iterare ogni riga del file in un ciclo for
    """
    for riga in a :
        print(riga)
    a.seek(0)
    
"""
Per trovare uno specifico carattere contenuto in un file
distinguiamo le lettere alfabetiche ed usiamo un separatore
"""


def trova_nonAlfa(testo : str) -> set[str]:
    #trovo i caratteri usati nel testo
    caratteri = set(testo)
    #ritorno solo quelli alfabetici
    return {c for c in caratteri if not c.isalpha()}


def leggi_parole(filename):
    #prima apriamo il file
    with open(filename,encoding = 'utf8',mode="r") as a:
        testo = a.read()
        #trasformo in minuscolo
        testo=testo.lower()
        
        #filtro i caratteri alfabetici con un altra funzione
        nonAlfa = trova_nonAlfa(testo)
        for carattere in nonAlfa:
            testo = testo.replace(carattere," ")
    print(testo)
leggi_parole("C:/Nuova cartella/ListaCose.txt")

    
    
    
    
    
    
    
    







    
    





