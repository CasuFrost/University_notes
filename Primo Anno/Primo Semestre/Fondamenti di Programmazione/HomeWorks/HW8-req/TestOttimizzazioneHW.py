import time
def clamp_values(x,y,limit):
    if x<0:
        x=0
    if y<0:
        y=0
    if x>limit[1]:
        x=limit[1]
    if y>limit[0]:
        y=limit[0]
    return x,y    
def Cambio_colori(tmpMatrix,turno,i,j,limit,DizComandi):
    for comandi in DizComandi:
        x = i+comandi[0]
        y = j+comandi[1]
        x,y=clamp_values(x,y,limit)
        if tmpMatrix[x][y]!=".":
            tmpMatrix[x][y]=turno
    return tmpMatrix
def is_valid_position(lista,turno,i,j,limit,DizComandi,dizTurni): 
    avversario = dizTurni[turno]
    for comandi in DizComandi:
        x = i+comandi[0]
        y = j+comandi[1]
        x,y=clamp_values(x,y,limit)
        if lista[x][y]==avversario:
            return True
    return False
def create_new_istant(lista,turno,i,j,limit,DizComandi,dizTurni):
    tmpMatrix = [[e for e in l] for l in lista]
    tmpMatrix[i][j]=turno   
    tmpMatrix=Cambio_colori(tmpMatrix,turno,i,j,limit,DizComandi)
    return tmpMatrix

def ricerca_ricorsiva(lista,turno,tripla,dizTurni,DizComandi,limit):
    
    
    haveValidPos=False
    W=0
    B=0
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if lista[i][j]=="." and is_valid_position(lista,turno,i,j,limit,DizComandi,dizTurni):  
                haveValidPos=True
                nuovaLista=create_new_istant(lista,turno, i, j, limit, DizComandi, dizTurni)
                ricerca_ricorsiva(nuovaLista,dizTurni[turno],tripla,dizTurni,DizComandi,limit)
            if lista[i][j]=="B":
                B+=1
                continue 
            if lista[i][j]=="W":
                W+=1
    if not haveValidPos:
        if B>W:
            tripla[0]+=1
        elif W>B:
            tripla[1]+=1
        else:
            tripla[2]+=1
def dumbothello(filename : str) -> tuple[int,int,int] :
    dizTurni = {"B":"W","W":"B"}
    DizComandi = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
    file=""
    lista=[]
    with open(filename, encoding = 'utf8') as f:
        file=f.read()
        a=file.split("\n")
    for i in a:
        if len(i.split())>0:
            lista.append(i.split())
    tripla = [0,0,0]
    limit = len(lista[0])-1,len(lista)-1
    ricerca_ricorsiva(lista,"B",tripla,dizTurni,DizComandi,limit)
    return tuple(tripla)   
if __name__ == "__main__":
    start=time.time()
    R = dumbothello("boards/08.txt")
    print(R)
    print(time.time()-start)