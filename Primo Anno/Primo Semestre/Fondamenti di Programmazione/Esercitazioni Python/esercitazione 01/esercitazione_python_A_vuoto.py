# -*- coding: utf-8 -*-
#
# Exercises by prof. Iacopo Masi
#
# %% evaluation
import evaluation

"""
Esercitazione-Python-A
Benvenuti!
"""

"""
# Esercitazione Python
# Autovalutazione su interi, float, stringhe, istruzioni condizionali, cicli
# iterare, liste, dizionari

# Premessa
Questa esercitazione serve per autovalutarvi. E' molto importante che
la svolgiate da parte vostra per farvi capire che esame e il corso è
molto **pratico** ed è necessario che vi allenate continuamente a
casa. Vi consente di capire quale è il vostro livello
(autovalutazione). In base al livello potete decidere se correre ai
ripari (e iniziare a fare più pratica su concetti di base) oppure
passare a concetti più avanzati.

Di seguito vengono riportati diversi piccoli problemi che dovete
risolvere implementando piccole funzionalità. I codici non sono mai
molto lunghi da scrivere quindi se vi trovate a scrivere paginate di
codice c'e' qualcosa che non va. L'esercitazione è divisa
in sezione dove ogni sezione affronta (piu o meno) argomento di base visti a lezione.
A differenza della lezione, c'e' da fare uno sforzo per capire come si applicano.
**Quindi cerchiamo di passare dalla teoria a farvi programmare nella
pratica perchè anche semplicemente copiare i comandi mentre io li
presento non vi insegna a programmare**

Gli esercizi sono (tendenzialmente) in ordine crescente di difficolta'.
"""

"""
# Parte 1: Interi e float e stringhe
"""


# %%01_int_to_str
"""
### Es. 1 - Banale
Scrivere una funzione che prende in ingresso un intero e rende una
stringa dell'intero

| input | output |
|-------+--------|
|     4 | '4'    |
|     7 | '7'    |
|     3 | '3'    |
|    10 | '10'   |
|   109 | '109   |
"""


def int_to_str(i):
    return str(i)


#evaluation.show_tests(int_to_str)
evaluation.evaluate(int_to_str)

# %% 02_int_to_str_flt
"""
### Es. 2 - Banale
Scrivere una funzione che prende in ingresso un intero e rende una
stringa dell'intero se l'intero è positivo oppure uguale a zero;
altrimenti rende la versione floating point dell'intero ma al contrario di segno.

| input | output |
|-------+--------|
|     4 |    '4' |
|    -7 |    7.0 |
|     3 |    '3' |
|   -10 |   10.0 |
|  -109 |  109.0 |
"""


def int_to_str_flt(i):
    if i >=0:
        return str(i)
    else:
        return(str(float(i*-1)))


evaluation.show_tests(int_to_str_flt)
#evaluation.evaluate(int_to_str_flt)

# %% 03_num_digits
"""
### Es. 3 - Facile
Scrivere una funzione che prende in ingresso un numero interi positivo
e torni il numero di cifre del numero (considerando il numero in base
10). Vedi tabella sottostante per esempi.

|  input | output |
|--------+--------|
|      4 |      1 |
|      7 |      1 |
|      4 |      1 |
|     10 |      2 |
|     23 |      2 |
|     45 |      2 |
|     99 |      2 |
|      0 |      1 |
|    100 |      3 |
|    222 |      3 |
|    999 |      3 |
| 999999 |      6 |
"""


def num_digits(intero):
    lista = list(str(intero))
    tmp=0
    for i in lista:
        tmp+=1
    return tmp


#evaluation.evaluate(num_digits)
evaluation.show_tests(num_digits)

# %% 04_num_digits_neg
"""
### Es. 4 - Banale
Modificare la funzione precedente in maniera tale che funzioni anche
con numeri negativi (se non funziona gia' come prima).  Nota da dentro
la funzione `num_digits_net` si puo richiamare la funzione vecchia per
controllare se funziona
"""

def num_digits_neg(v):
    pass


#evaluation.evaluate(num_digits_neg)
evaluation.show_tests(num_digits_neg)

# %% 05_num_digits_neg_str_mix
"""
### Es. 5 - Banale
Implementare la stessa funzione ma questa volta l' input può essere
sia un intero anche negativo che una stringa Potete riusare le
funzionalità precedenti se volete

| input     | output |
|-----------+--------|
| '4'       |      1 |
| -7        |      1 |
| '0002'    |      1 |
| 10        |      2 |
| '0999999' |      6 |
"""


def num_digits_neg_str_mix(v):
    pass

#evaluation.evaluate(num_digits_neg_str_mix)
evaluation.show_tests(num_digits_neg_str_mix)

# %% 06_check_int_str
"""
###Es. 6 - Facile
Sia data una stringa in ingresso alla funzione e un intero anche
negativo. La funzione deve ritornare il numero di volte che questo
intero è nella stringa.

Ad esempio dato gli input:

'p-1pp-1', -1

la funzione deve rendere 2 in quanto -1 è contenuto 2 volte nella stringa.

| input         | output |
|---------------+--------|
| 'pippo', 1    |      0 |
| 'pippo1', 2   |      0 |
| 'pippo2', 2   |      1 |
| 'p1pp0', 0    |      1 |
| 'p1pp1', 1    |      2 |
| 'p-1pp-1', -1 |      2 |
"""


def check_int_str(stringa, intero):
    pass


#evaluation.evaluate(check_int_str)
evaluation.show_tests(check_int_str)

# %% 07_check_S_in_T
"""
###Es. 7 - Facile/Medio
Scrivere una funzione che prende in ingresso una stringa S (di soli
numeri) e una strinag T che contiene sia numeri che caratteri. La
funzione renda una lista dove ogni elemento contiene il conteggio di
ogni **SINGOLO** numero di S rispetto all stringa T.
Il conteggio inserito nella lista è allineato alla lista in uscita.

Dati:

S = '1234'
T = 'p1p2p335o'

si deve rendere [1,1,2,0]

in quanto
- '1' è contenuto 1 volta in T
- '2' è contenuto 1 volta in T
- '3' è contenuto 2 volte in T.
- '4' è contenuto 0 volte in T.
"""


def check_S_in_T(S, T):
    pass


#evaluation.evaluate(check_S_in_T)
evaluation.show_tests(check_S_in_T)


# %% 08_count_sub_string
"""
### Es. 8  Medio
Data una stringa "query" in input e un'altra stringa "corpo", e'
necessario trovare tutte le volte che "query" è contenuta nella
stringa "corpo"

query = 'pippo'
corpo = 'pipppippopipipipipippppppippo'

output = 2

in quanto pippo è contenuta 2 volte in corpo infatti se marchiamo
PIPPO in corpo appare in:
corpo = 'pippPIPPOpipipipipipppppPIPPO'
              1                    2

NB: NON SI PUO' USARE IL METODO count() delle stringhe
"""


def count_sub_string(query, corpo):
    pass


evaluation.show_tests(count_sub_string)
#evaluation.evaluate(count_sub_string)

# %% 09_count_sub_string_idx
"""
### Es. 09 Medio
Dato l'esercizio precedente, modifica la funzione al fine di
restituire una lista di tuple. La lista è cosi fatta.  Ciascuna
elemento della lista è una tupla. La tupla contiene gli indici di
inizio e terminazione della sotto stringhe `query` trovata nella
stringa `corpo`.

Se in ingresso abbiamo:

query = 'pippo'
corpo = 'pipppippopipipipipippppppippo'
         012345678

deve rendere:
output = [(4, 8), (24, 28)]

in quanto:
- corpo[4] vale 'p' (p iniziale di pippo)
- corpo[8] vale 'o' (o finale di pippo)

pippo si trova dall'indice 4 all'indice 8 compreso.

Inoltre si trova anche a:
- corpo[24] vale 'p' (p iniziale di pippo)
- corpo[28] vale 'o' (o finale di pippo)
"""


def count_sub_string_idx(query, corpo):
    pass


#evaluation.evaluate(count_sub_string_idx)
evaluation.show_tests(count_sub_string_idx)

# %% 10_check_reverse
"""
### Es. 10 - Facile
Vengono date due stringhe in ingresso ed è necessario controllare se
la prima stringa `S` è stata scritta al rovescio rispetto alla stringa
`T`.

T = 'pippo'
S = 'oppip'

allora S è stata scritta al rovescio.

Mentre

```python
T = 'pippo'
S = 'opppp'
```
non lo è.

Scrivere una funzione check_reverse(S, T) che prende in ingresso due
stringhe e ritorni True se sono a rovescio, altrimenti False.
"""


def check_reverse(S, T):
    pass


#evaluation.evaluate(check_reverse)
evaluation.show_tests(check_reverse)


"""
# Parte 2: Liste, Tuple, Ordinamento, Dizionari
"""

#%% 11_sum_max_min
"""
###Es. 11 Banale
Data una lista in ingresso L ritornare una tupla che contiene
1. al primo elemento la somma di tutti i valori nella lista
2. al secondo elemento il massimo di tutti i valori
3. al terzo elemento il minimo
"""


def sum_max_min(L):
    pass


#evaluation.evaluate(sum_max_min)
evaluation.show_tests(sum_max_min)

#%% 12_sum_positive
"""
### Es. 12  Banale 
Dalla funzione sottostante che prende in ingresso una
lista `L` sommare tutti i valori positivi

L = [10, 5, -5, -20, -30, -1, 20]

restituire 35.
"""


def sum_positive(L):
    pass


#evaluation.evaluate(sum_positive)
evaluation.show_tests(sum_positive)

# %% 13_list_multipli
"""
### Es. 13 Medio
Data la funzione sottostante che prende in ingresso una lista `L` è
necessario restituire una lista che contiene nella PRIMA parte della
lista i valori multipli di 2 della lista L, nella SECONDA parte della
lista valori multipli di 5 della lista L. L'ordine di inserimento
segue come sono messi i valori nella lista originale L.

L = [10, 5, -5, -20, -30, -1, 20]

rende

 [10, -20, -30, 20, 10, 5, -5, 20, -30, 20]
 #  multipli di 2       |  multipli di 5
"""


def list_multipli(L):
    pass

#evaluation.evaluate(list_multipli)
evaluation.show_tests(list_multipli)

# %% 14_cum_sum
"""
### Es. 14 - Facile
Data la funzione sottostante che prende in ingresso una lista L e'
necessario creare e rendere come output un' altra lista che contiene
all' elemento i-esimo la somma cumulata degli elementi della lista L
precedenti all'elemento i-esimo, con questo ultimo compreso nella somma.

L = [-9, 42, 6]

rende 

output = [-9, 33, 39]
"""


def cum_sum(L):
    pass


#evaluation.evaluate(cum_sum)
evaluation.show_tests(cum_sum)


# %% 15_get_list_except_min_max
"""
###Es. 15 - Medio/Difficile
Completare la funzione sottostante che data una lista in ingresso `L`
modifica la suddetta lista L in maniera tale da non avere più il
valore minimo e il massimo. La funzione modifica la lista L **senza
creare una altra lista (si modifica quella in input IN-PLACE)**.
La funzione rende il minimo e il massimo. La lista L NON puo' essere
vuota.

NB: si assume che il minimo e il massimo NON abbiano duplicati.
Ossia, il minimo e massimo sono unici.

L = [0, 5, 42, -1, 5, 3, 23]

modifica L in maniera tale che dopo sia:

L = [0, 5, 5, 3, 23]

e rende -1, 42.

Altro esempio:

L = [0, 4]

rende 0, 4 e L = []
"""

def get_list_except_min_max(L):
    pass

    
#evaluation.evaluate(get_list_except_min_max)
evaluation.show_tests(get_list_except_min_max)

#%% 16_get_list_except_min_max_general
"""
### Es. 16 - Medio/Difficile
Data una lista `L` in ingresso alla funzione modificare la lista
L in-place (SENZA CREARNE UNA COPIA) in maniera da eliminare il minimo
 e il massimo e restituire il numero totale di elementi eliminati.
 
1) La lista in ingresso puo' essere vuota.
2) Il massimo e minimo valore possono NON essere unici.
3) il minimo e il massimo possono coincidere.

1)
L = [5, 5, 5, 5, 5]

L si modifica in []
rende 5.

2)
L = [-11, 13, -11,  13, -11]

L si modifica in []
rende 5

3)
L = [-5, 2, -5, 10, -11, -11, 10, 0, -11, 2]

L si modifica in [-5, 2, -5, 0, 2]
rende 5

4)
L = []

si modifica L in []
rende 0
"""

def get_list_except_min_max_general(L):
    pass

evaluation.show_tests(get_list_except_min_max_general)
#evaluation.evaluate(get_list_except_min_max_general)


# %% 17_reshape_by_index
### Es. 17 - Difficile
'''
Sono date in ingresso tre liste di lunghezza uguale di nome
 `L`, `src`, e  `dst`.
E' necessario creare una nuova lista `out` in uscita con le seguenti
proprietà:
- dato l'elemento i-esimo nella lista `L`,  
    la nuova lista deve contenere il valore preso alla posizione i-esima
    delle lista `src`. Questo valore deve essere scritto nella posizione indicata
    dall'elemento i-esimo della lista `dst`.

- Nota bene: i valori di dst fanno si che alcuni elementi della lista in uscita
non vengano scritti. In questo caso il loro valore intero deve essere None.
    
L =   [4, 2, 1, -5]
src = [1, 2, 3,  0]     # indici di quali valori prendere da L
dst = [2, 4, 6,  8]     # indici di dove mettere i valori nel risultato

deve rendere:

out = [None, None, 2, None, 1, None, -5, None, 4] 
     
'''

def reshape_by_index(L, src, dst):
    pass


evaluation.show_tests(reshape_by_index)
#evaluation.evaluate(reshape_by_index)


#%% 18_list_to_tuple
"""
###Es. 18 Medio
E' fornita in ingresso una lista L di tuple ed è necessario tornare
come valore di ritorno una tupla di liste. Le tuple possono avere
lunghezza variabile. E' necessario tornare come output una tupla di
liste. Ciascuna lista dentro la tupla di ritorno contiene i valori al
contrario rispetto alle tuple iniziali.  Le liste nella tupla da rendere
contengono valori il cui prodotto e' multiplo di 2.

L = [(2, -2, 4 ), (2, -2, 1 ), (0, 5, 4 ), (1,3), (1, 1, 5, 11)]

rende 

out = ([4, -2, 2], [1, -2, 2], [4, 5, 0])
"""

def list_to_tuple(L):
    pass

evaluation.show_tests(list_to_tuple)
#evaluation.evaluate(list_to_tuple)

#%% 19_sort_by_str
"""
###Es. 19 - Medio/Difficile
Dati in ingresso una tupla T di stringhe restituire una tupla S che ordina
la tupla suddetta T in ordine crescente in base alla lunghezza delle
parole e in ordine decrescente in base all'ordine lessicografico.

T = ('aaaaa', 'aaa', 'zzzzz', 'zzz')

S = ('zzz', 'aaa', 'zzzzz', 'aaaaa')
"""

def sort_by_str(T):
    pass


evaluation.show_tests(sort_by_str)
#evaluation.evaluate(sort_by_str)


#%% 20_sort_by_month
"""
###Es. 20  - Difficile

Data in ingresso una lista con i nomi dei mesi restituire un'altra
lista ordinata in base all'ordine dei mesi nel calendario.

NB: i nomi dei mesi possono avere l'iniziale sia in UPPER case che 
lower case. Quindi 'Gennaio' e' valido cosi come 'gennaio'.

a)
L = ['Settembre', 'luglio', 'gennaio', 'Maggio']

deve rendere

['gennaio', 'Maggio', 'luglio', 'Settembre']

in quanto gennaio viene prima di tutti, poi segue
Maggio poi luglio e infine Settembre secondo il calendario.
"""

def sort_by_month(L):
    # trovate qui per riferimento i mesi gia' ordinati
    # vi fa comodo pensate a come usarlo
    mesi = ['gennaio','febbraio', 'marzo','aprile','maggio','giugno','luglio',
            'agosto','settembre','ottobre','novembre','dicembre']
    pass


#evaluation.evaluate(sort_by_month)
evaluation.show_tests(sort_by_month)


#%% 21_int_to_hist
"""
###Es. 21 Difficile

Data in ingresso una lista di interi `L` è necessario generare una stringa
che visualizza a video il conteggio di ogni singolo intero sottoforma di un
ISTOGRAMMA.

L = [1, 1, 1, 1, 4, 4, 4, 5, 5, 10, 10]

e' necessario che la funzione torni una stringa uguale a 

'1\t****\n2\t\n3\t\n4\t***\n5\t**\n6\t\n7\t\n8\t\n9\t\n10\t**\n'

che se stampata mostra l'ISTOGRAMMA degli interi dove:
- il numero di volte (frequenza) che in intero appare in L e' rappresentato numero
di asterischi uguali alla frequenza.
- ISTOGRAMMA ha su ciascuna riga il seguente formato:
   valore \t  * per quante volte e' presente e infine \n (accapo)"
- se un numero non e' presente non va stampato nessun asterisco.

Ad esempio la stringa in uscita dalla funzione int_to_hist quando prende in 
ingressso L e':



1	****
2	
3	
4	***
5	**
6	
7	
8	
9	
10	**


"""

def int_to_hist(values):
    pass

evaluation.show_tests(int_to_hist)
#evaluation.evaluate(int_to_hist)


#%% 22_anagramma
"""
###Es. 22

Data in ingresso due stringhe S e T la funzione deve controllare se le
due stringhe sono una l'anagramma dell'altra. Ritorna True se lo sono
altrimenti torna False.

Data una strinag S, un anagramma si crea permutando (spostando di posizione)
 i caratteri della stringa S ma senza aggiungere ne rimuovere caratteri.

S = 'roma'
T = 'amor'

la coppia e' un anagramma perche' 'roma' puo' essere generata da 
'amor' semplicemente spostando alcuni caratteri.

S = 'a gentleman'
T = 'elegant man'

anche questa coppia lo e'.

S = 'fiore'
T = 'eroii'

NON lo e'. 
"""

def anagramma(S, T):
    pass

evaluation.show_tests(anagramma)
#evaluation.evaluate(anagramma)
