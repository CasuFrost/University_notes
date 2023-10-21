
"""
02/12/2022
Dalla prima diramazione si crea un sotto albero sinistro ed un sotto albero destro
ogni volta che vogliamo fare un operazione possiamo ragionare sui due alberi 
ed ottenere le soluzioni dei due sotto alberi
"""

class NodoBinario:
    def __init__(self, V:int,left : 'NodoBinario'=None,right : 'NodoBinario'=None):
        self._value=V
        self._sx = left
        self._dx = right
    def __repr__(self):
        return f'NodoBinario({self._value})'
        
def stampa_PRE(radice : NodoBinario,livello : int = 0) -> None:
    print("|--"*livello,radice)
    if radice:
        stampa_PRE(radice._sx,livello+1)
        stampa_PRE(radice._dx,livello+1)
        
def stampa_POST(radice,livello=0):
    if radice:
        stampa_POST(radice._sx,livello+1)
        stampa_POST(radice._dx,livello+1)
    print("|--"*livello,radice)
n11=NodoBinario(11)
n10=NodoBinario(10)
n00=NodoBinario(20)
n1=NodoBinario(1,right=n11,left=n00)
n0=NodoBinario(0,left=n10)
r=NodoBinario(100,n0,n1)
stampa_PRE(r)

#trova il percorso più lungo nell'albero
def altezza2(radice,profondita=0):
    if radice is None:
        return profondita
    P_sx = altezza2(radice._sx,profondita+1)
    P_dx = altezza2(radice._dx,profondita+1)
    return max(P_sx,P_dx)

print(altezza2(r))

#nodo con più di 2 figli
class NodoNario:
    def __init__(self, V : int, sons:list['NodoNario']=None):
        self._value=V
        if sons is None:
            self._sons=[]
        else:
            self._sons = sons
    #def altezza ( [son.altezza()=1 for son in self._sons],default=0)
    
    
    
n1 = NodoNario(1) 
n2 = NodoNario(2) 
n3 = NodoNario(3) 

n123=NodoNario(123,[n1,n2,n3])

def stampa_PRE_nario(radice : NodoNario,livello : int = 0) -> None:
    print("|--"*livello,radice)
    if radice:
        for i in radice._sons:
            stampa_PRE_nario(i._sons,livello+1)
            
stampa_PRE_nario(n123)      
