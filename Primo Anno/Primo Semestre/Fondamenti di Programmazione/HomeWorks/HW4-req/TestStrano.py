import time
# -*- coding: utf-8 -*-
'''
Obiettivo dello homework è leggere alcune stringhe contenute in una serie di
file e generare una nuova stringa a partire da tutte le stringhe lette.
Le stringhe da leggere sono contenute in diversi file, collegati fra loro a
formare una catena chiusa. Infatti, la prima stringa di ogni file è il nome di
un altro file che appartiene alla catena: partendo da un qualsiasi file e
seguendo la catena, si ritorna sempre nel file di partenza.

Esempio: il contenuto di "A.txt" inizia con "B.txt", il file "B.txt", inizia
con "C.txt" e il file "C.txt" inizia con "A.txt", formando la catena
"A.txt"-"B.txt"-"C.txt".

Oltre alla stringa con il nome del file successivo, ogni file contiene anche
altre stringhe separate da spazi, tabulazioni o caratteri di a capo. La
funzione deve leggere tutte le stringhe presenti nei file della catena e
costruire la stringa che si ottiene concatenando i caratteri con la più alta
frequenza in ogni posizione. Ovvero, nella stringa da costruire, alla
posizione p ci sarà il carattere che ha frequenza massima nella posizione p di
ogni stringa letta dai file. Nel caso in cui ci fossero più caratteri con
la stessa frequenza, si consideri l'ordine alfabetico.
La stringa da costruire ha lunghezza pari alla
lunghezza massima delle stringhe lette dai file.

Quindi, si deve scrivere una funzione che prende in ingresso una stringa A 
che rappresenta il nome di un file e restituisce una stringa.
La funzione deve costruire la stringa secondo le indicazioni illustrate sopra
e ritornare le stringa così costruita.

Esempio: se il contenuto dei tre file A.txt, B.txt e C.txt nella directory
test01 è il seguente

test01/A.txt          test01/B.txt         test01/C.txt                                                                 
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite                                                                       
garden                park                 hello                                                                       
kitchen               affair               portrait                                                                     
balloon                                    angel                                                                                                                                               
                                           surfing                                                               

la funzione most_frequent_chars("test01/A.txt") dovrà restituire la stringa
"hareennt".
'''

def check_line(riga,listaStringhe):
    i = riga.strip()
    if i!="":
        if ("\t" in i or " " in i):            
            tmp = i.split()
            for j in tmp: 
                listaStringhe.append(j)
        else:      
            listaStringhe.append(i)
        
def Exctract_string_from_file(filename,originalFilename,listaStringhe):  
    with open(filename,encoding = 'utf8') as StringFile:
        line = StringFile.read()
        tmpList = line.split()
        if originalFilename== tmpList[0]:
            listaStringhe+= tmpList[1:]
            return 0
        else:
            listaStringhe+= tmpList[1:]
            Exctract_string_from_file(tmpList[0],originalFilename,listaStringhe)

def build_string_list(filename):  
    listaStringhe = [] #Questa sarà la lista che conterrà tutte le stringhe all'interno della catena dei file
    listaStringhe=Exctract_string_from_file(filename,filename,listaStringhe)

    return  listaStringhe #ritorno tutte le stringhe all'interno della catena dei file esclusi gli spazi vuoti
    

def stringList_to_finalString(lista):
    
    listaDizionari = []
    stringa = ""
    lenght = len(max(lista, key=len))
    listaDizionari = [{} for i in range(lenght)]
    for parola in lista:          
        for i,carattere in enumerate(parola): 
            #print(i,carattere)
            if carattere in listaDizionari[i]:
                listaDizionari[i][carattere]=listaDizionari[i][carattere]+1
            else:                
                listaDizionari[i][carattere] = 1
                
    for i in listaDizionari:    
       # print(i)
        maxValue = 0
        listaLettere = []
        for j in i.keys():
            if i[j]>maxValue:
                maxValue=i[j] 
        #print(max(i, key=i.get))
        for j in i.keys():
            if i[j]==maxValue:
                listaLettere.append(j)            
        listaLettere.sort()
        stringa+=listaLettere[0] 

    return stringa

def most_frequent_chars(filename: str) -> str:
    # SCRIVI QUI LA TUA SOLUZIONE
    ListaStringhe=[]
    Exctract_string_from_file(filename,filename,ListaStringhe)
    return stringList_to_finalString(ListaStringhe)

valori = []
start = time.time()

most_frequent_chars("test01/A.txt")
most_frequent_chars("test02/bullfight.txt")
most_frequent_chars("test03/woodchuck.txt")
most_frequent_chars("test04/pampers.txt")
most_frequent_chars("test05/avocados.txt")
most_frequent_chars("test06/strums.txt")
most_frequent_chars("test07/sinew.txt")
most_frequent_chars("test08/boilings.txt")
most_frequent_chars("test09/meddles.txt")
most_frequent_chars("test10/aileron.txt")
most_frequent_chars("test11/metonymies.txt")
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
print("tempo impiegato : ",round(sum(valori)/len(valori),2))
#print(a)

"""
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
start = time.time()
most_frequent_chars("test12/incipience.txt")
end = time.time()
valori.append(round(end - start,2))
print("tempo medio impiegato : ",round(sum(valori)/len(valori),2))

#most_frequent_chars("test12/incipience.txt")

         ('test02/bullfight.txt', 'poternusakesness'),
         ('test03/woodchuck.txt', 'aanreeaseesable'),
         ('test04/pampers.txt', 'ceeelieessseds'),
         ('test05/avocados.txt','sereeieeesssssncy'),
         ('test06/strums.txt', 'sereeeeesssssssynssm'),
         ('test07/sinew.txt', 'すひびずじぞぜぃけそみきおょぇどべしこしこれれあねきゞ゜ぷ'),
         ('test08/boilings.txt', '🚏🏞😨♣☢🐸‼🗻🌚🥷🍯🎽♾🗽🍄⚔🫓😠🍈🪀🏞➡🍼👩😻📿🌁🕌👾🤓😚®❇💒🦪👒💂☪🥡🥕'),
         ('test09/meddles.txt', 'ᛢᚦᛝᛡᚤᚬᚬᛍᚸᛘᚣᚢᛜᛥᚳᛜᛖᛄᚢᛊᚬᛟᛈᛅᛞᚹᛯᚼᛁᚺ'),
         ('test10/aileron.txt', 'ᛠᚣᚻᛝᚧᛜ᛭くᚻᛝᚭᛈᚺᛦᚩᛞᛏᚽᛪᚢᚰᚯひᛃだᚯᚨろᚷᚦᛕᚸᛯᛄᛩᛂᚲᛆᛏᚰᛨぼゆᛇᛮᛚᚯᛓやᚼかᚯᚨᛦ᛫ᚩᚲᛋᚽ👘♒ぜ🕋ゔ🕣📬💊☺🦌'),
         ('test11/metonymies.txt', 'ᛃᚬᛝᚸᛈᚦᚱᛦᛢᛮᚼᛋᚯᛤᚳᛈᛓᚿᛊᚬᛈᚯᛎᚦᛅᛮᚧᚬᛦᚲᚮᚶᛑきᛓᛔᛮぞᛘᚼᛤᚩᛮᚼᛋᛛᛡᚱᛌᛑᚩᛪきᛤᛃᛅᛞᛏᛣᚤᚻᚦᚢᚩᛨᛐᛘゔᚷᚴᚧᚺᛖᛑᛨᛈがᛃᛥᚽᛚᚣᛋᚾᚳᚩごばᚩᚰぐがたᚨᚼᚩᛉ゜ᛅᚬᚲぅしᛪᚵᚨぎᛝᛡᛀごでᛟᚸゖそぇが🏟🃏じゔᚫぴ💌🔸😖ᛆᛪᚯ᛫ᚤᛑᚺᚾᛒᛦにぼ゙ぞゃせねねな'),
         ('test12/incipience.txt', 'sereeeeeesssssssりᚷᛈᚳᚽᚿᚪᛙᛪᛄᚩᚿᛨᚧᚮめわᛂᛆᛘᛤᛤᛜᛉᛈᚣのぽᚳᛅᚺᛊᛛᚪᚶᚡᛘᚷᚥᛑ᛬ᛋᚥᚩᚮᛏᛅᛎᚯᚱᚽしᚻᛔᚳᛇᚪᛅᚲᚪᛨᛒゐᚨᚰᚽᚩᚿつげᛊつᚢだᛇᚺᛯᚮりᚬᚴᚹよょぬおᚱᛮᛏᚹᛑᚮっᛋ🛢ᚲᛢ📲ぃᚭᛡゐぴ🆖🫒⏰👹🍹ᛅ⏏◀🛄👍🌽🔥🎅🆙🦒🦟🔤🚓😗😕ᛦᛃᛮᛈᛂ'),
         )
"""