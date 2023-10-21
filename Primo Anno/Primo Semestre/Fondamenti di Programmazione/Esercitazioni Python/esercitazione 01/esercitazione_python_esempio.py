#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%% evaluation
import evaluation

"""
Esercitazione-Python-A
Benvenuti!
"""

"""Es.1 Scrivere una funzione che prende in ingresso un intero e rende come 
output il valore al cubo dell'intero

| input | output |
|-------+--------|
|     4 | 64     |
|     7 | 343    |
|     3 | 27     |
"""

#%% cubo
def cubo(i):
    return i**3

# Mostra i casi di test su cui e' valutata la funzione
#evaluation.show_tests(cubo)
# valutazione: eseguire questa parte solo
# quando avete finito di scrivere la funzione
evaluation.evaluate(cubo)

#%% Altro-ex
print('Altro esercizio')