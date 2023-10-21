# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import images

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Scrivere una funzione che data una matrice di interi, restituisce la matrice trasposta
# Ad esempio:
# 5 2 9    ->  5 3
# 3 1 0        2 1
#              9 0
def transpose(m : List[List[int]]) -> List[List[int]]:
    finalMatrix = []
    cnt = 0
    listIndex = 0
    for i,riga in enumerate(m[0]):
        for j,colonna in enumerate(m[1]):
            if j==i:
                tmp=[riga,colonna]            
                finalMatrix.append(tmp)
                listIndex+=1
    return finalMatrix

# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente alla somma fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       2 2 2
#     2 1 1   +    2 3 1   =   4 4 2
#     0 1 1        4 2 2       4 3 3
#     1 1 2        1 2 3       2 3 5
# Restituire None se le due matrici non possono essere sommate.
def matrix_matrix_sum(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    finalList = []
    if len(A)!=len(B):
        return None
    for i in range(len(A)):
        if len(A[i])!=len(B[i]):
            return None
    for i in range(len(A[0])+1):
        
        tmp = []
        for j in range(len(A[1])):
            tmp.append(A[i][j]+B[i][j])
            #print(A[i][j]+B[i][j])
        finalList.append(tmp)
        
    return finalList
                #print(i,j)
"""
 [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], 
 [[1, 2], [2, 3], [4, 2], [1, 2]]
"""
# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente al prodotto fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       5  4 3
#     2 1 1   x    2 3 1   =   8  9 5
#     0 1 1        4 2 2       6  5 3
#     1 1 2                    11 9 6
# Restituire None se le due matrici non possono essere moltiplicate.
"""
[[1, 0, 1], 
 [2, 1, 1], 
 [0, 1, 1], 
 [1, 1, 2]], 

[[1, 2, 1], [2, 3, 1], [4, 2, 2]]
"""
def matrix_matrix_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    if len(A[0])>len(B):
        return None
    matriceFinale=[]
    for i in range(len(A)):
        tmp=[]
        
        matriceFinale.append(tmp)
    #print(len(matriceFinale)==len(A))
    for i,riga in enumerate(A): 
        #qui i assume l'indice della rigaù
        for j,colonna in enumerate(B[0]):
            tmpList=[]
            for k,rigaDiA in enumerate(riga):
                tmpList.append(rigaDiA*B[k][j])
            matriceFinale[i].append(sum(tmpList))
                
                        
                        #tmpList.append(A[i][KI]*B[j][KJ])
            #matriceFinale[i][j]=sum(tmpList)
            #qui j assume l'indice della colonna
        
    return matriceFinale

    #print(matriceFinale)

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine rotata di 90 gradi a destra e invertita rispetto l'asse verticale.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_rotate_right_and_flip_v(img_in: str, img_out : str):
    lista = images.load(img_in)
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            pass
    
    images.save(lista[::-1],img_out)

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine con i canali rosso e blu invertiti.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_invert_channels(img_in: str, img_out : str):
    lista = images.load(img_in)
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            lista[i][j]=lista[i][j][::-1]
    images.save(lista,img_out)
    
# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui ognuno dei 3 canali è quantizzato su 128 possibili valori (cioè, ogni canale può solo assumere 128 valori anzichè 256).
# Ad esempio, (21, 126, 3) diventa (10, 63, 2)
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_quantize(img_in: str, img_out : str):
    lista = images.load(img_in)
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            listaColore=[]
            for colore in range(len(lista[i][j])):
                listaColore.append(int((lista[i][j][colore]*128)/255))
            lista[i][j]=tuple(listaColore)
    images.save(lista,img_out) 
           


# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui la metà destra dell'immagine è scambiata con la metà sinistra.
# (Cioè, le colonne nel range [0, N/2] diventano le colonne [N/2, N] nella nuova immagine,
# e le colonne [N, N/2] nella vecchia immagine diventano le colonne [0, N/2] nella nuova immagine).
# Si può assumere che l'immagine abbia un numero di colonne divisibile per 2.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_invert_half(img_in: str, img_out : str):
    lista = images.load(img_in)
    width = len(lista[0])
    halfWidth = width/2
  
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if j > halfWidth:
                
                
                lista[i][j],lista[i][int(j-halfWidth)]=lista[i][int(j-halfWidth)],lista[i][j]
               
            else:
                pass
    images.save(lista,img_out)   

# Test funzioni
check_test(transpose, [[5, 3], [2, 1]], [[5, 2], [3, 1]])
check_test(transpose, [[5, 3], [2, 1], [9, 0]], [[5, 2, 9], [3, 1, 0]])
check_test(transpose, [[5, 3]], [[5], [3]])
check_test(transpose, [[5], [3]], [[5, 3]])
check_test(matrix_matrix_sum, [[2, 2, 2], [4, 4, 2], [4, 3, 3], [2, 3, 5]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2], [1, 2, 3]])
check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2], [2, 3], [4, 2], [1, 2]])
check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
check_test(matrix_matrix_mul, [[5, 4, 3], [8, 9, 5], [6, 5, 3], [11, 9, 6]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
check_test(matrix_matrix_mul, [[5], [8], [6], [11]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1], [2], [4]])
check_test(matrix_matrix_mul, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1]])
img_rotate_right_and_flip_v("img1.png", "img1_rotate_flip.png")
img_invert_channels("img1.png", "img1_invert_channels.png")
img_quantize("img1.png", "img1_quantized.png")
img_invert_half("img1.png", "img1_inverted_half.png")