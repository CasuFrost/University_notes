#IMMAGINI

black = 0,0,0
white = 255,255,255

import images #BISOGNA IMPORTARE LA LIBRERIA IMMAGINI
"""
L'immagine è una matrice di pixel, usiamo due liste, una lista esterna contiene
i pixel orizzontali, quella interna i pixel verticali
ogni pixel è rappresentato da una tupla di 3 valori (R,G,B)
"""

def crea_immagine_arrata(larghezza,altezza,colore):
    riga = [colore]*larghezza
    img = [riga]* altezza
    return img


def crea_imm(L,H,C):
    img = []
    for y in range(L):
        riga = []
        for x in range(H):
            riga.append(C)
        img.append(riga)

images.visd(crea_imm(100,100,(255,0,0)))


try:
    pass
    #codice potenzialmente errato
except  :
    pass
    #codice da eseguire se Tipo di erroe






