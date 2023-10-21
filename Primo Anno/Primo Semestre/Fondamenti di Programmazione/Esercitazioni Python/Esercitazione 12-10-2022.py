from typing import Any, Callable, List


# Stampa un test
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'ERROR: {func_str}({args_str}) => {error_str}')


################################################################################
# Stringhe
################################################################################


# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    return "Ciao "+name+" Buona giornata!"

# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    lunghezza = len(string)
    counter = 0
    ListaCaratteri = list(string)
    while(ListaCaratteri[0+counter]==" "):
        ListaCaratteri[0+counter]=""
        counter+=1
    counter=0 
    while(ListaCaratteri[(lunghezza-1)-counter]==" "):
        ListaCaratteri[(lunghezza-1)-counter]=""
        counter+=1
    stringaStrippata=""
    for x in ListaCaratteri:
        stringaStrippata+=x
    return  stringaStrippata


# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str ) -> List[str]:
    listaCaratteri = list(string)
    stringaSplittata=""
    for x in listaCaratteri:
        if x == characters:
            x=""
        stringaSplittata+=x
    return stringaSplittata


# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    wordsList = string.split(" ")
    stringaSostituita=""
    for x in wordsList:
        if x == find:
            x = replace
        stringaSostituita+=x
        stringaSostituita+=" "
    return stringaSostituita


# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    CryptedString = ""
    listaStringa = list(string)
    if decrypt==False:
        for x in listaStringa:
            x=chr(ord(x) + offset)
            CryptedString+=x
    else:
        for x in listaStringa:
            x=chr(ord(x) - offset)
            CryptedString+=x
    return CryptedString
        

# Scrivere una funzione che controlla la validita' di una password.
# La password deve avere:
# - Almeno una lettera fra [a-z] e una lettera fra [A-Z]
# - Almeno un numero fra [0-9]
# - Almeno un carattere fra [$#@]
# - Essere lunga almeno 6 caratteri
# - Essere lunga non piu' di 16 caratteri
# - La password non è valida se contiene caratteri diversi da quelli specificati sopra
#   o se viola una delle regole specificate.
# La funzione restituisce true/false a seconda se la password sia valida o meno.
def check_pwd(pwd: str) -> bool:
    notAllowedChar = False
    CapsLetterValidity = False
    LetterValidity = False
    NumberValidity = False
    SpecialValidity = False
    listaPwd = list(pwd)
    for x in listaPwd:
        if ord(x) >= 65 and ord(x)<=90:
            CapsLetterValidity=True
        elif ord(x) >= 97 and ord(x)<=122:
            LetterValidity=True
        elif ord(x) >= 48 and ord(x)<=57:
            NumberValidity=True
        elif x == "$" or x == "#" or x == "@" :
            SpecialValidity=True
        else:
            notAllowedChar=True
    if len(pwd) >= 6 and  len(pwd)<=16:
        if CapsLetterValidity and LetterValidity and NumberValidity and SpecialValidity and notAllowedChar==False:
            return True
        else:
            return False
    else:
        return False
      


# Test funzioni
print_test(make_hello, 'Pippo')
print_test(strip_whitespace, '  Pippo  ')
print_test(strip_whitespace, '   ')
print_test(split_string, 'Pippo Pluto  ', 'P')
print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
print_test(replace_substring, 'Ciao Pippo. Ciao Pluto.', 'Ciao', 'Hello')
print_test(caesar_cypher, 'ciao pippo', 12, False)
print_test(caesar_cypher, 'oum{,|u||{', 12, True)
print_test(check_pwd, "a")
print_test(check_pwd, "000000000000000000")
print_test(check_pwd, "almeno6")
print_test(check_pwd, "Aa@09asng2/")
print_test(check_pwd, "Aa@09asng2")

################################################################################
# Liste
################################################################################


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    Sum = 0
    for x in elements:
        Sum+=int(x)
    return Sum


# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    Max = 0
    for x in elements:
        if x>Max:
            Max=x
    return Max

# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    pass


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    newList = []
    lenght = len(elements)
    while lenght>0:
        newList.append(elements[lenght-1])
        lenght-=1
    return newList
# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e ritorna una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    finalList = []
    for x in elements: 
        if isinstance(x,list):
            for y in x:
                if isinstance(y,list):
                    for z in y:
                        finalList.append(z)
                else:
                    finalList.append(y)
        else:
            finalList.append(x)
    return finalList

# Test funzioni
print_test(sum_squares, [1, 2, 3])
print_test(max_element, [1, 2, 3, -1, -2])
print_test(remove_duplicates, [1, 2, 3, 2, 3])
print_test(reverse_list, [1, 2, 3, 4, 5])
print_test(flatten_list, [[-1,0],1, [2, 3],[4, 5,[9,7]]])
