# -*- coding: utf-8 -*-
"""
d esempio:
1)           catRL
            /   \
           o     i
costruisce l'immagine  i|o, visibile aprendo expected_img_01.png

"""
lista_z = ['catLR',
           ['flip_v',
            ['flip_v', ['image_c.png', None, None] , None],
            None,
            ],
           ['flip_v',
            None,
            ['flip_v', None, ['flip_v',
                              ['image_a.png', None, None], None]
             ],
            ]
           ]
import images
import tree

a = tree.BinaryTree.fromList(lista_z)

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
#images.save(concatena(images.load("image_o.png"),images.load("PROVAFOTO.png"),"catRL"),"s.png")

ex3(a,"TESTICOLO.png")



syllables  = ['bos', 'co', 'sa']
expected = ['boscosa', 'bossaco', 'cobossa', 'cosabos', 'sabosco', 'sacobos',
 'bosco', 'bossa', 'cobos', 'sabos', 'cosa', 'saco']


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


print(ex4(syllables)==expected)













