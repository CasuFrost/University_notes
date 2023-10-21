
for y in range(5):
    print(y)
    
diz = {6:'x','b':2, 'porcaccioddio':'LVCE'}

print(diz[6])


#per estrarre chiave ed elemento in un ciclo for è utile utilizzare il metodo dei dizionari "items()"
for chiave,elemento in diz.items():
    print(chiave,elemento)
    
    
#Iterare per gli indici di una lista
lista = ['a','b','c']

for i in range(len(lista)):    
    print(i)
    

#che succede se durante l'iterazione della lista la MODIFICO?
#Esempio :
for i in range(len(lista)):    
    if i == 3:
        del(lista[i])
#L'elemento 3 viene eliminato, il Quarto elemento viene spostato sul terzo,
#la lista continua ad iterare con il nuovo quarto perdendosi il valore precedente. Inoltre
#Si avrà un errore con l'ultimo elemento della lista


#Se una lista/contenitore/tupla è vuoto, in un IF assumerà valore False, se invece
#ha almeno UN valore, varrà True


lista = []
if lista:
    print("ciao")

lista=[1,2,3]
if lista:
    print("tutto ok?")











