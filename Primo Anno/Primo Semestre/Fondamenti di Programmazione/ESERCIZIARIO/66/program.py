
import albero
l=[0, [-1, None, None],[1, [0, None, None],[2, None, None],],]
uno = albero.AlberoBinario.fromList(l)
print(uno)
print("*"*50)
#print(uno)


def search(tree,listValue,deep):
    print("deep: ",deep)
    if deep<listValue[0]:
        listValue[0]=deep
    if deep>listValue[1]:
        listValue[1]=deep
    ogDeep=deep
    if tree.sx!=None:
        deep-=1
        search(tree.sx,listValue,deep)
    if tree.dx!=None:
         ogDeep+=1
         search(tree.dx,listValue,ogDeep)  

        
        

        
def es66(tree):
    listValue=[0,0]
    deep=0
    deepSx=0
    #print(tree)
    search(tree,listValue,deep)

    print(listValue)
    return abs(listValue[1]-listValue[0])
    """
    Es  17: 9 punti - ricorsivo

    Si definisca la funzione es66, ricorsiva (o che fa uso di vostre funzioni ricorsive) che:
    - riceve come argomento un AlberoBinario (definito nel file albero.py)

    Calcola la "larghezza massima" dell'albero,  ovvero la differenza tra 
    la posizione del nodo che si trova piu' a destra nell'albero
    e la posizione del nodo che si trova piu' a sinistra.
    Per calcolare la posizione di un nodo rispetto alla radice (che assumiamo sia a posizione 0)
    basta sottrarre 1 (uno) ogni volta che si scende su un sottoalbero sinistro
    ed aggiungere 1 (uno) ogni volta che si scende su un sottoalbero destro.
    Esempio: se l'albero e' quello qui sotto a sinistra le posizioni saranno quelle nell'albero a destra
             1           .            0         .
            / \          .           / \        .
           2   3         .         -1   1       .
          / \            .        /  \          .
        4    5           .      -2    0         .
       /    /            .      /    /          .
      6    7             .    -3    -1          .
       \    \            .      \    \          .
        8    9           .      -2    0         .
    Il nodo piu' a sinistra (6) e' a posizione -3
    mentre quello piu' a destra (3) e' a posizione 1
    Quindi la funzione torna il valore 4=1-(-3)
    """
    # inserite qui il vostro codice
print(es66(uno))