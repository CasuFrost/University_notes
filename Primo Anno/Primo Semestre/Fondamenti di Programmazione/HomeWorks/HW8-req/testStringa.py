
def is_space_valid_pos(i,istante,DizComandi,dizTurni,ValoriStruttura):
    valid=False
    copiaIstante=[[],[],[],istante[3]]
    for comandi in DizComandi:
        x=i[0]+comandi[0]
        y=i[1]+comandi[1]
        if (x,y) in istante[ValoriStruttura[dizTurni[copiaIstante[3]]]]:
            if valid==False:
                for j in range(3):
                    copiaIstante[j]=istante[j].copy()  
                valid=True
            copiaIstante[ValoriStruttura[dizTurni[copiaIstante[3]]]].remove((x,y))
            copiaIstante[ValoriStruttura[copiaIstante[3]]].append((x,y))
    
    if valid: 
        copiaIstante[ValoriStruttura[copiaIstante[3]]].append(i)
        copiaIstante[ValoriStruttura["."]].remove(i)
        copiaIstante[3]=dizTurni[copiaIstante[3]]
        return copiaIstante
    return False
 
   
def elaborazione_ricorsiva_strutturaDati(istante,dizTurni,DizComandi,ValoriStruttura,triplaStruttura,dictAlberature):    
    haveValidPos=False
    if str(istante) in dictAlberature:
        pass
        #print(dictAlberature[str(istante)])
        if dictAlberature[str(istante)]=="B":
            return (triplaStruttura[0]+1,triplaStruttura[1],triplaStruttura[2])
        if dictAlberature[str(istante)]=="W":
            return (triplaStruttura[0],triplaStruttura[1]+1,triplaStruttura[2])
        else:
            return (triplaStruttura[0],triplaStruttura[1],triplaStruttura[2]+1)

    for i in istante[ValoriStruttura["."]]:
        nuovoIstante = is_space_valid_pos(i,istante,DizComandi,dizTurni,ValoriStruttura)
        if nuovoIstante:
            haveValidPos=True
            elaborazione_ricorsiva_strutturaDati(nuovoIstante,dizTurni,DizComandi,ValoriStruttura,triplaStruttura,dictAlberature)
     
    if not haveValidPos:
        
        if len(istante[0])>len(istante[1]):
            triplaStruttura[0]+=1
            dictAlberature[str(istante)]="B"
            return triplaStruttura
        elif len(istante[0])<len(istante[1]):
            triplaStruttura[1]+=1
            dictAlberature[str(istante)]="W"
            return triplaStruttura
        else:
            dictAlberature[str(istante)]="P"
            triplaStruttura[2]+=1
            
    return triplaStruttura
def dumbothello(filename : str) -> tuple[int,int,int] :
    dizTurni = {"B":"W","W":"B"}
    DizComandi = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
    ValoriStruttura={"B":0,"W":1,".":2,"turno":3}
    file=""
    dictAlberature={}
    lista=[]
    istante=[[],[],[],"B"]
    with open(filename, encoding = 'utf8') as f:
        file=f.read()
        a=file.split("\n")
    for i in a:
        if len(i.split())>0:
            lista.append(i.split())
    
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if lista[i][j]=="B":
                
                istante[0].append((i,j))
            if lista[i][j]=="W":
                
                istante[1].append((i,j))
            if lista[i][j]==".":
               
                istante[2].append((i,j))
        
    
    triplaStruttura = [0,0,0]
    
    elaborazione_ricorsiva_strutturaDati(istante,dizTurni,DizComandi,ValoriStruttura,triplaStruttura,dictAlberature)
    
    
    return tuple(triplaStruttura)  
import time
if __name__ == "__maain__":
    R = dumbothello("boards/08.txt")
    print("tupla finale = ",R)
if __name__ == "__main__":
    media=[]
    for i in range(1,10):
        start=time.time()
        R = dumbothello("boards/0"+str(i)+".txt")
        #R = dumbothello("boards/09.txt")
        #print(R)
        media.append(time.time()-start)
    print(round(sum(media),3))
    