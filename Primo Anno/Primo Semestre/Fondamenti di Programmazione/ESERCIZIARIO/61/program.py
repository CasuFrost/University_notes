
def sumTripleValue(lista):
    maxx=[]
    for i in lista:
        somma=0
        for j in i:
            somma+=j
        maxx.append(somma)
    return maxx


def minTripleValue(lista):
    maxx=[]
    for i in lista:
        maxtmp=100000000000
        for j in i:
            if j<maxtmp:
                maxtmp=j
        maxx.append(maxtmp)
 
    return maxx

def maxTripleValue(lista):
    maxx=[]
    for i in lista:
        maxtmp=0
        for j in i:
            if j>maxtmp:
                maxtmp=j
        maxx.append(maxtmp)
 
    return maxx
def es61(ftesto, op, sel):
    mat=[]
    with open(ftesto) as F:
        Line=F.readline().strip().split()
        while len(Line)>0:
            mat.append(Line)
            Line=F.readline().strip().split()
    rows=[]
    cols=[]
    dp=[]
    sp=[]
    for i in range(len(mat)):
        tmpRow=[]
        for j in range(len(mat[0])):
            tmpRow.append(int(mat[i][j]))
            #print(i,j,mat[i][j])
        rows.append(tmpRow)
    cntCol=0
    #COLS
    
    
    for i in range(len(mat)):
        tmpCols=[]
        for j in range(len(mat[0])):
            
                tmpCols.append(int(mat[j][i]))
        
        cols.append(tmpCols)
        
        
    cnt=len(mat[0])-1
    cnt2=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j == cnt:
                sp.append(int(mat[i][j]))
                cnt-=1
                
            if j == cnt2:
                dp.append(int(mat[i][j]))
        cnt2+=1
        
        
    print(cols)
    d=[]
    tipla=[]
    if sel=="dp":
        d[:]=dp
    if sel=="ds":
        d[:]=sp
    if sel=="row":
        tipla[:]=rows
    if sel=="col":
        tipla[:]=cols
    
    if sel=="dp" or sel=="ds":
        if op=="sum":
            return [sum(d)]
        if op=="min":
            return [min(d)]
        if op=="max":
            return [max(d)]
    else:
        if op=="sum":
            return sumTripleValue(tipla)
        if op=="min":
            return minTripleValue(tipla)
        if op=="max":
            return maxTripleValue(tipla)
    
    '''
    La funzione es62(ftesto, op, sel) che, legge una matrice di interi contenuta
    nel file di testo ftesto e restituisce una lista di interi.
    La matrice e' memorizzata nel file per righe con  gli interi nelle righe separati da un numero
    arbitrario di spazi.
    La lista da tornare contiene i risultati di una operazione da effetture sulle righe, le colonne
    o le diagonali della matrice. Il parametro 'op' specifica il tipo di operazione, e
    puo' assumere tre diversi valori:
        'max' (per il calcolo del massimo),
        'min' (per il calcolo del minimo)
        e 'sum' (per il calcolo della somma).
    Il parametro 'sel' specifica su quali elementi della matrice  l'operazione deve operare.
    puo' assumere i seguenti valori:
        'row' (per applicarla alle varie righe della  matrice, in ordine crescente),
        'col' (per applicarla alle varie colonne della  matrice, in ordine crescente),
        'dp' (per applicarla  alla diagonale principale)
        e 'ds' per applicarla alla diagonale  secondaria.
    Ad esempio se la matrice contenuta nel file di testo e':
    2  0   -4
    5  10  20
    5  1   -1

    a seconda dei parametri si avra':

    es61(ftesto, 'max','row')= [2, 20, 5]
    es61(ftesto, 'min','row')= [-4, 5,-1]
    es61(ftesto, 'sum','row')= [-2, 35, 5]
    es61(ftesto, 'max','col')= [ 5,  10, 20]
    es61(ftesto, 'min','col')= [ 2,  0, -4]
    es61(ftesto, 'sum','col')= [ 12, 11, 15]
    es61(ftesto, 'max','dp' )= [10]
    es61(ftesto, 'min','dp' )= [-1]
    es61(ftesto, 'sum','dp' )= [11]
    es61(ftesto, 'max','ds' )= [10]
    es61(ftesto, 'min','ds' )= [-4]
    es61(ftesto, 'sum','ds' )= [11]
    '''
    # inserisci qui il tuo codice
print(es61("matrice4.txt","max","ds"))