img_in = 'ex2/image01.png'
colors = {(255,0,0):(10,20), (0,255,0):(30,40), (255,0,255):(10,10)}
import images
def ord_dict(diz):
    
    for i in diz:
        for j in diz:
            if diz[i][0]>diz[j][0]:
                print(i,diz[i])
            elif diz[i][0]==diz[j][0]:
                if diz[i][1]>diz[j][1]:
                    i
                    tmp = i
                    i = j
    
    for j in diz:
        print(j,diz[j],"x = ",diz[j][0],"y = ",diz[j][1])
   
def draw_rect_in_position(Matrice,pos,Dimension,color):
   
    TotOg=pos
    xOrigin = pos[0]
    yOrigin = pos[1]
    maxx=pos[0]+Dimension[0]
    while(pos[0]<=maxx-2):
        pos=(pos[0]+1,pos[1])
        Matrice[pos[0]][pos[1]]=color
    pos=(xOrigin,pos[1]+Dimension[1]-1)    
    while(pos[0]<=maxx-2):
        pos=(pos[0]+1,pos[1])
        Matrice[pos[0]][pos[1]]=color 
     
    pos=TotOg
    
    maxx=pos[1]+Dimension[1]
    while(pos[1]<=maxx-2):
        pos=(pos[0],pos[1]+1)
        Matrice[pos[0]][pos[1]]=color 
        
    pos=(pos[0]+Dimension[0]-1,yOrigin)    
    while(pos[1]<=maxx-2):
        pos=(pos[0],pos[1]+1)
        Matrice[pos[0]][pos[1]]=color 
        
        
def ex2(img_in, img_out, colors):
    newDiz = {}
    
    Matrice = images.load(img_in)
    for i in range(len(Matrice)-1,0,-1):
        for j in range(len(Matrice[0])-1,0,-1):
            for k in colors.keys():
                if k == Matrice[i][j]:
                    newDiz[k]=(i,j,colors[k])
    ord_dict(newDiz)
   
    for i in range(len(Matrice)-1,0,-1):
        for j in range(len(Matrice[0])-1,0,-1):
            for index in range(len(newDiz)-1,-1,-1):
            
                pos = (list(newDiz.items())[index][1][0],list(newDiz.items())[index][1][1])
                if pos==(i,j):
                    draw_rect_in_position(Matrice,pos,list(newDiz.items())[index][1][2],list(newDiz.items())[index][0])
    images.save(Matrice,img_out)           
    #ord_dict(newDiz)
ex2(img_in,"prova.png",colors)