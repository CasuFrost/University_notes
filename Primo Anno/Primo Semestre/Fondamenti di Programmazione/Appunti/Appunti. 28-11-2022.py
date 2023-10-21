# -*- coding: utf-8 -*-
"""
Un problema ammette ricorsione se :
    é possibile rimipicciolire la dimensione del problema
    esiste un problema che ha una soluzione elementare (caso base)
    è sempre possibile applicando ripetutamente la riduzione, arrivare al caso base
    
Un classico esempio è il fattoriale

"""
def somma_ricorsiva(L):
    if L:
        primo,*resto=L
        return primo * somma_ricorsiva(resto)
    else: return 0
    
def somma_iter(L:list[int])->int:
    somma=0 
    N = len(L)
    for i in range(N):
        somma+=L[i]
    return somma

