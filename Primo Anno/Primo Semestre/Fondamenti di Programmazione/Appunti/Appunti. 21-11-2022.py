# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Programmazione ad oggetti
"""
Ogni oggetto ha : 
    Attributi : i dati che caratterizzano una particolare entità
    
    Metodi : Le funzioni di una particolare entità
    
    Le entità si chiamano classi e ogni individuo è un istanza di esso
    
"""


"""
Definira una classe

class NomeDellaClasse(EstendendoLaClasse): Tra parentesi si passa la classe dalla quale viene estesa

    attributo_di_classe = valore
    def __init__(self,<argomenti>): La funzione __init__ vale da costruttore 
        self.attributo_individuale = valore1
        
"""

def clamp(i,minimo,massimo):
    if i < minimo:
        return minimo
    if i > massimo:
        return massimo
    return i

def clamp_color(i):
    if i < 0:
        return 0
    if i > 255:
        return 255
    return i

import images


class Colore :
    black : 'Colore'
    def __init__(self,R : float,G:float,B:float):
        self.R = clamp_color(R)
        self.G = clamp_color(G)
        self.B = clamp_color(B)
    
    def white():
        return Colore(255,255,255)
    def __add__(self,other):
        #Ritorno la somma di 2 colori
        return Colore(self.R+other.R,self.G+other.G,self.B+other.B)
    
    def negativo(self):
        return Colore.white()-self
        
rosso = Colore(255,0,0)
#Sfrutto il metodo add per creare un colore nuovo
bianco = rosso.__add__(Colore(0,255,255))





class Image:
    def __init__(self,  larghezza : [int]=None,
                        altezza : [int]=None,
                        sfondo : [Colore]=None,
                        filename : [str]=None):
        if filename:
            img = images.load(filename)
            self.img =  [[ Colore(R,G,B) for R,G,B in riga]for riga in img]
        else:
            pass
    def __repr__(self):
        return f"immagine({self._W}x{self._H})"
    
    def AsTriples(self):
        return [[c.AsTriples() for c in riga] for riga in self.img]
    
    #def visualizza(self):
     #   return images.visd(AsTriples())

   
cane = Image(filename="images/luna.png")
print(cane.img)






