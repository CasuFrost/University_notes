# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:17:42 2022

@author: mcasu
"""

import images
import time
import imagesDebug as images2
def bordi(img, next_position):
    lunghezza = len(img) - 1
    larghezza = len(img[0]) - 1
    if next_position[0] > larghezza:
        next_position[0] = 0
    elif next_position[0] < 0:
        next_position[0] = larghezza
    if next_position[1] > lunghezza:
        next_position[1] = 0
    elif next_position[1] < 0:
        next_position[1] = lunghezza
    return next_position

def diagonali(img, verde, next_position, this_position):
    next_position = bordi(img, next_position)
    if img[next_position[1]][this_position[0]] == verde and img[this_position[1]][next_position[0]] == verde:
        return True
    else:
        return False

def verifica(img, out_img, position, rosso, nero, arancione, grigio, verde, this_position, next_position, lista, last_pixel):
    if img[next_position[1]][next_position[0]] == rosso or img[next_position[1]][next_position[0]] == verde:
        return False
    if img[next_position[1]][next_position[0]] == arancione:
        this_position = next_position.copy()
        img[this_position[1]][this_position[0]] = verde
        lista.append(this_position)
    if img[next_position[1]][next_position[0]] == nero or img[next_position[1]][next_position[0]] == grigio:
        this_position = next_position.copy()
        img[this_position[1]][this_position[0]] = verde
        lista.append(this_position)
        last_pixel = lista[0]
        img[last_pixel[1]][last_pixel[0]] = grigio
        lista.pop(0)

def corpo(commands, start_img, position, out_img, rosso, nero, arancione, grigio, verde):
    img = images.load(start_img)
    stringhetta = commands.split()
    this_position = position
    next_position = position.copy()
    last_pixel = position.copy()
    lista = [position]
    img[position[1]][position[0]] = verde
    stoppete = False
    stoppete_porcocan = True
    cnt = 0
    speed=0
    for a in stringhetta:
        time.sleep(speed)
        cnt+=1
        images2.visd(img)
        if cnt==97:
            speed=0.5
        if a == 'NW':
            next_position[0] = this_position[0] - 1
            next_position[1] = this_position[1] - 1
            stoppete = diagonali(img, verde, next_position, this_position)
        elif a == 'N':
            next_position[1] = this_position[1] - 1
            next_position = bordi(img, next_position)
        elif a =='NE':
            next_position[0] = this_position[0] + 1
            next_position[1] = this_position[1] - 1
            stoppete = diagonali(img, verde, next_position, this_position)
        elif a == 'W':
            next_position[0] = this_position[0] - 1
            next_position = bordi(img, next_position)
        elif a == 'E':
            next_position[0] = this_position[0] + 1
            next_position = bordi(img, next_position)
        elif a == 'SW':
            next_position[0] = this_position[0] - 1
            next_position[1] = this_position[1] + 1
            stoppete = diagonali(img, verde, next_position, this_position)
        elif a == 'S':
            next_position[1] = this_position[1] + 1
            next_position = bordi(img, next_position)
        elif a == 'SE':
            next_position[0] = this_position[0] + 1
            next_position[1] = this_position[1] + 1
            stoppete = diagonali(img, verde, next_position, this_position)
        
        if stoppete:
            print("namio")
            break
        stoppete_porcocan = verifica(img, out_img, position, rosso, nero, arancione, grigio, verde, this_position, next_position, lista, last_pixel)
        if stoppete_porcocan == False: break
        this_position = next_position
    images.save(img,out_img)
    lunghez = len(lista)
    return lunghez

def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    rosso = 255, 0, 0
    nero = 0, 0, 0
    arancione = 255, 128, 0
    grigio = 128, 128, 128
    verde = 0, 255, 0
    return corpo(commands, start_img, position, out_img, rosso, nero, arancione, grigio, verde)
 
print("lunghezza serpente = ",generate_snake("./data/input_04.png", [19, 35], "S S S S W W W W N N N N N N E E E E E E E N E S S S E E E E S E S E S E S E S E N N N N N N N E N E E N E N N E N E N E N E N E N N W N W N W N W W W N W N W N W N W W W N N N N E N N E N E E E E NE NE NE NE S NW SW NE NE S SE S E W S W N E NW SE S NW NW NE SE NE S S E SW W NE NE S W NW SE S S SE NE N SW SW NW NW S S N SE SW E SE SW NW NW SW SW NE W W N SE SW S S SW S SW S S S W S E N NW NW SW S NE S SW SE NE S NW W NE W N S S SW NE SW NE SW SW NE W SW SE E W N SW W NE SE SE S W SE NW NW N E NE SW NW SW W NE NW NW NE S N E NE NE N N E E S NW SW NW E NW NE S E SW N W NE S NW NE N N N N NW SW S SW NW SW SW W NW SW SW E SE W W W NE SE SE S E S SE E W NW SE NE S SW E NW NW S SE S N W NE NW SW S E S E S NW SW S E S NW N SW N W W NE E E N N E E S W NE SE NW E SW S SW N W S S NE NW SW NE NE N W S SE SE S SE S W N S N N NW NW NW S SE S S S SW E W NE NE NW SW W N NW W NW W S N N NE NE S S W SW S N E S NW SW N" , "./output/expected_end_04wrong.png"))
