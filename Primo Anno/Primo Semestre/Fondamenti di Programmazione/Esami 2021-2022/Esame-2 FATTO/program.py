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

# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Esercizio 1: 6 punti

Si scriva una funzione ex1(file_db, k) che prende in ingresso il nome
di un file di testo file_db, mentre k e' un intero. Il file contiene una
sequenza di stringhe separate da spazi e/o ritorni a capo, ad esempio:

  hola this
  
              is
    a                        sequence

La funzione deve leggere il contenuto del file e calcolare la somma
tra le lunghezze di tutte le coppie di stringhe, nell'ordine seguente:
per prima la coppia formata dalla prima stringa e dalla seconda, poi
quella formata dalla prima e la terza, poi la prima e la quarta, e così via;
poi la seconda stringa e la terza, la seconda e la quarta, e così via;
poi la terza e la quarta, la terza e la quinta...

Nell'esempio sopra, le coppie saranno considerate e indicizzate come segue:

 index | lunghezza1 | lunghezza2 | somma |
   0   |     5      |     4      |   8   | (hola + this)
   1   |     5      |     2      |   6   | (hola + is)
   2   |     5      |     1      |   5   | (hola + a)
   3   |     5      |     8      |   12  | (hola + sequence)
   4   |     4      |     2      |   6   | (this + is)
   5   |     4      |     1      |   5   | (this + a)
   6   |     4      |     8      |   12  | (this + sequence)
   7   |     2      |     1      |   3   | (is + a)
   8   |     2      |     8      |   10  | (is + sequence)
   9   |     1      |     8      |   9   | (a + sequence)

La funzione, considerando le coppie in ordine decrescente di somma,
deve ritornare gli indici delle k coppie che hanno la somma delle
lunghezze più alta in assoluto.
Nel caso in cui la somma delle lunghezze per due coppie sia identica,
le due coppie mantengono l'ordine che avevano quando sono state prese
in considerazione inizialmente (vedere colonna "index" nell'esempio qui sopra).

Ad esempio, se k=2 e file_db contiene:

  hola this
  
              is
    a                        sequence

le coppie saranno considerate e indicizzate come nella tabella sopra
e la funzione dovrà restituire la lista di indici:
[3, 6]


"""

def ex1(file_db, k):
    ListaParole=[]
    with open(file_db) as F:
        ListaParole[:]=F.read().split()
    checkedWords=[]
    listaCoppie=[]
    index=0
    for i in ListaParole:
        for f in ListaParole:
            if i!=f and f not in checkedWords:
                listaCoppie.append((i,f,len(i)+len(f),index))
                index+=1
        checkedWords.append(i)
    
    for i in range(len(listaCoppie)):
        for j in range(len(listaCoppie)):
            if listaCoppie[i]!= listaCoppie[j]:
                if  listaCoppie[i][2]> listaCoppie[j][2]:
                    tmp= listaCoppie[i]
                    listaCoppie[i]= listaCoppie[j]
                    listaCoppie[j]=tmp
                    
    
    return [listaCoppie[i][3] for i in range(k)]

"""
Esercizio 2: 8 punti

Abbiamo in ingresso due interi H e W che definiscono altezza e
larghezza di un'immagine. Dobbiamo creare una immagine di dimensioni
HxW salvarla al percorso 'img_out'.
In ingresso abbiamo una lista 'pts' di punti 2D, ciascun punto
contiene le coordinate float x, y e una lista 'colors' di colori RGB
come ad esempio:
               x      y        x     y      x     y
    pts    = [[17.0, 48.0], [34.0, 94.0], [6.0, 95.0]]
                r   g   b     r   g   b     r    g    b
    colors = [[117, 85, 80], [79, 83, 68], [67, 143, 134]]

Il primo punto [17.0, 48.0] e' associato al primo colore [117, 85, 80]
e cosi via.

Per ogni coppia di coordinate P=(x, y) dell'immagine dobbiamo trovare
l'indice I del punto piu' vicino rispetto ai punti in 'pts' in base
alla distanza d = |x1-x2| + |y1-y2|. In caso di parita' sulla distanza
 si mantiene l'ordine di ingresso dei colori.

Il pixel dell'immagine alla posizione P = (x, y) verra' colorato usando il
colore che si trova all'indice I del piu vicino.  Ad esempio se i punti
sono 'pts' mostrati sopra e la coordinata dell'immagine vale P = (2, 1)
allora il piu vicino risulta il punto con indice I=0 in quanto le
distanze sono:

P = (2, 1)
| indice I |  0 |   1 |  2 |
| x        | 17 |  34 |  6 |
| y        | 48 |  94 | 95 |
| dist     | 62 | 125 | 98 |

e quindi il pixel (2, 1) verra' colorato di [117, 85, 80].

Vanno poi disegnati i punti 'pts' di colore nero (0, 0, 0),
arrotondando le coordinate con int. I punti 'pts' sono tutti dentro
l'immagine  (6 punti)

Il primo caso di test genera l'immagine in 'ex2/ex2_1_expected.png'
mentre il tuo risultato e' in 'ex2_your_result_img_1.png'

Infine si deve togliere tutti i punti da 'pts' in maniera distruttiva.
(+2 punti).

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""
def modulo(i):
    if i>=0:
        return i
    else:
        return i*-1
import images

def ex2(H, W, pts, colors, img_out):
    matrice=[[(0,0,0) for i in range(W)] for i in range(H)]
    pts.reverse()
    colors.reverse()
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            
            distances=[]
            maxx=0
            for k in range(len(pts)):
                distances.append(modulo(j-pts[k][0])+modulo(i-pts[k][1]))
                if distances[k]==min(distances):
                    maxx=distances[k],k
                #print(pts[k],i,j)
            if  matrice[i][j]==(0,0,0):
                matrice[i][j]=colors[maxx[1]]
                
            
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            
            for k in pts:
                
                if [i,j]==[int(k[1]),int(k[0])]:
                    matrice[i][j]=(0,0,0)
                    pts.remove(k)
    
    images.save(matrice,img_out)
    return pts

# %% ----------------------------------- EX.3 --------------------------------- #
"""
Esercizio 3: 10 punti (3+3+3+1)

Abbiamo delle immagini che vogliamo combinare tra loro mediante
una serie di operazioni. La sequenza di operazioni è rappresentata
mediante un albero binario che ha come valori delle stringhe. In
particolare
- le foglie dell'albero contengono stringhe che puntano al percorso delle
  immagini su disco;
- i nodi interni sono stringhe che indicano le operazioni da svolgere sui
  propri sottoalberi.

I nodi interni possono rappresentare operazioni binare o unarie, a seconda
del numero di figli. Le operazioni sono:
- 'catLR': due immagini left e right si concatenano orizzontalmente
   sistemando left alla sinistra di right.
- 'catRL': due immagini left e right si concatenano orizzontalmente
   sistemando right alla sinistra di left.
NB: è garantito che le immagini da unire hanno sempre la stessa altezza.
- 'flip_v': un'immagine viene rovesciata (flip) rispetto all'asse
   verticale. Ossia ᴐ diventa c.

In caso di nodo con operazioni binaria, l'operazione indicata
nell'attributo value si applica al risultato delle operazioni dei
sottoalberi sinistro e destro. In caso di nodo unario, l'operazione
indicata si applica al solo sottoalbero presente.

Si progetti una funzione ex3 ricorsiva o che fa uso di funzioni
ricorsive che:
- prende in ingresso un oggetto root di classe BinTree che
  punta al nodo radice di un albero binario che modella operazioni
  su immagini, come descritto sopra;
- carica le immagini alle foglie;
- esegue le operazioni descritte dai nodi interni sui sottoalberi
  fino a costruire l'immagine rappresentata dalla radice;
- salva l'immagine ottenuta alla radice in un file indicato dal percorso
  'saved_image'
- restituisce una tupla contenente altezza e larghezza dell'immagine
  costruita e salvata.

Nota: Dato un nodo, si accede al figlio sinistro e destro con gli
attributi left e right. Per chiarimenti, fare riferimento al file 
tree.py. L'attributo value di ogni nodo contiene sempre una stringa.

Ad esempio:
1)           catRL
            /   \
           o     i
costruisce l'immagine  i|o, visibile aprendo expected_img_01.png

2)             catLR
              /     \
            catRL    o
           /    \
        catRL  flip_v
        /   \       \
       a     i       ᴐ

costruisce l'immagine  c|i|a|o, visibile aprendo expected_img_03.png
"""

import images
import tree

def concatena(l,r,comand):
    if comand=="catLR":
        #print(len(l[0])+len(r[0]))
        newFoto=[["" for i in range(len(l[0])+len(r[0]))]for i in range(len(l))]
        #print(len(newFoto[1]))
        for i in range(len(l)):
            for j in range(len(newFoto[1])):
                if  j<=len(l[0])-1:
                    
                    #print(i,j,len(r),len(r[0]))
                    #print(len(l[0]))
                    newFoto[i][j]=l[i][j]
                else:        
                    
                    newFoto[i][j]=r[i][j-len(l[0])]
    else:
        newFoto=[["" for i in range(len(l[0])+len(r[0]))]for i in range(len(l))]
        for i in range(len(l)):
            for j in range(len(newFoto[1])):
                if  j<=len(r[0])-1:   
                    newFoto[i][j]=r[i][j]
                else:  
                    newFoto[i][j]=l[i][j-len(r[0])]
                #print(j)
    return newFoto
    
def flip_photo(root):
    if "png" in root.value:
        #print(root.value)
        foto=images.load(root.value)
        w=len(foto[0])
        newFoto=[["" for i in range(w)] for i in range(w)]
        for i in range(len(foto)):
            for j in range(len(foto[0])-1,-1,-1):
                newFoto[i][j]=foto[i][w-j-1]
        return newFoto
    else:
        if root.left:
            a = flip_photo(root.left)
            w=len(a[0])
            newFoto=[["" for i in range(w)] for i in range(w)]
            for i in range(len(a)):
                for j in range(len(a[0])-1,-1,-1):
                    newFoto[i][j]=a[i][w-j-1]
            return newFoto
        else:
            a = flip_photo(root.right)
            w=len(a[0])
            newFoto=[["" for i in range(w)] for i in range(w)]
            for i in range(len(a)):
                for j in range(len(a[0])-1,-1,-1):
                    newFoto[i][j]=a[i][w-j-1]
            return newFoto
    
def ex3rec(root):
    neww=0
    if root.value=="flip_v":
        if root.left:
            return flip_photo(root.left)
        else:
            return flip_photo(root.right)
        
        #IL codice deve prendere il nodo figlio e flipparlo
    elif "png" in root.value:
        return images.load(root.value)
    else:
        #il codice deve costruire un immagine dai propri figli
        foto=concatena(ex3rec(root.left),ex3rec(root.right),root.value)
        #print(len(foto[0]))
        return foto
        
def ex3(root, saved_image):
    #INSERISCI QUI IL TUO CODICE
    foto=ex3rec(root)
    images.save(foto,saved_image)
    return (len(foto),len(foto[0]))







# %% ----------------------------------- EX.4 ----------------------------------- #
'''
Esercizio 4: 9 punti

    È data in input una lista di sillabe e si vuole costruire
    la lista di tutte le stringhe che si possono generare combinando due o più
    di tali sillabe.
    Scrivere una funzione ex4(syllables) ricorsiva o che fa uso di funzioni
    o metodi ricorsivi che individui tutte le stringhe che è possibile
    generare usando le sillabe nella lista syllables.
    La funzione può ritornare un insieme con tutte le stringhe
    individuate (6 punti). La funzione può opzionalmente ritornare una
    lista senza ripetizioni ordinata in ordine decrescente per numero di
    caratteri, in caso di parità in ordine alfabetico (+3 punti).
    
    Es: se syllables = ['bos', 'co', 'sa'] allora la funzione
    ritorna (6 punti):
    {'bossa', 'cobossa', 'sacobos', 'cosabos', 'bosco', 'boscosa',
     'sabos', 'saco', 'bossaco', 'cobos', 'sabosco', 'cosa'} (6 punti)
    oppure ritorna (9 punti):
    ['boscosa', 'bossaco', 'cobossa', 'cosabos', 'sabosco', 'sacobos',
     'bosco', 'bossa', 'cobos', 'sabos', 'cosa', 'saco'] (8 punti)
    ''' 

def rec4(syllabes,lista):
    for i in syllabes:
        for j in syllabes:
            if i!=j:
                k=i+j
                if i+j not in lista:
                    lista.append(i+j)
                nuovaL=[i+j]
                nuovaL=syllabes.copy()
                nuovaL.remove(i)
                nuovaL.remove(j)
                nuovaL.append(i+j)
                if len(nuovaL)>1:
                    rec4(nuovaL,lista)
                
        
def ordinaLista(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i]!=lista[j]:
                if len(lista[j])<len(lista[i]):
                    tmp = lista[i]
                    lista[i]=lista[j]
                    lista[j]=tmp
                if len(lista[j])==len(lista[i]):
                    tmp=max([lista[j],lista[i]])
                    if tmp==lista[j]:
                        lista[j]=lista[i]
                        lista[i]=tmp
        
def ex4(syllables):
    lista=[]
    rec4(syllables,lista)
    ordinaLista(lista)
    print(lista)
    return lista
    return lista

###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print(ex4(['bos', 'co', 'sa']))
    print('ciao')
