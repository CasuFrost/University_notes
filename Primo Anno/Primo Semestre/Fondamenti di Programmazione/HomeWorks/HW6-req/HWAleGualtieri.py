

import time
import imagesDebug as images

def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
   # Scrivi qui il tuo codice
    immaggine=images.load(start_img)
    comandi= commands.split()
    testaY= position[1]
    testaX= position[0]
    larghezza=len(immaggine[0])
    altezza=len(immaggine)
    arancione=(255,128,0)
    rossa=(255,0,0)
    scia=(128,128,128)
    verde=(0,255,0)
    posizione=[testaY,testaX]
    corpo= [(tuple(posizione))]
    immaggine[testaY][testaX]= (0,255,0)
    for comando in comandi:
        images.visd(immaggine)
        time.sleep(0.02)
        if comando=="S":
            immaggine[corpo[0][0]][corpo[0][1]]=scia
            testaY+=1  
        if comando=="N": 
            testaY-=1
            immaggine[corpo[0][0]][corpo[0][1]]=scia
        if comando=="W":
            testaX-=1
            immaggine[corpo[0][0]][corpo[0][1]]=scia
        if comando=="E":
            testaX+=1
            immaggine[corpo[0][0]][corpo[0][1]]=scia
        if comando=="NW":
            testaY-=1
            testaX-=1
            immaggine[corpo[0][0]][corpo[0][1]]=scia
            if (testaY+1,testaX) in corpo and (testaY,testaX+1) in corpo:
                immaggine[corpo[0][0]][corpo[0][1]]=verde
                break
        if comando=="NE":
            testaY-=1
            testaX+=1
            immaggine[corpo[0][0]][corpo[0][1]]=scia
            if (testaY+1,testaX) in corpo and (testaY,testaX-1) in corpo:
                immaggine[corpo[0][0]][corpo[0][1]]=verde
                break
        if comando=="SW":
            testaY+=1
            testaX-=1
            immaggine[corpo[0][0]][corpo[0][1]]=scia
            if (testaY-1,testaX) in corpo and (testaY,testaX+1) in corpo:
                immaggine[corpo[0][0]][corpo[0][1]]=verde
                break
        if comando=="SE":
            testaY+=1
            testaX+=1
            immaggine[corpo[0][0]][corpo[0][1]]=scia
            if (testaY-1,testaX) in corpo and (testaY,testaX-1) in corpo:
                immaggine[corpo[0][0]][corpo[0][1]]=verde
                break
            
            
         
        if testaX==-1:
            testaX=larghezza-1 
        if testaX==larghezza:
            testaX=0
        if testaY==altezza:
            testaY=0  
        if testaY==-1:
            testaY=altezza-1
            
     
      #  testaY,testaX,immaggine=pacman(testaY, testaX, altezza, larghezza)
         
        if immaggine[testaY][testaX]==arancione:
            corpo.append((testaY,testaX)) 
            immaggine[testaY][testaX]=verde
        elif immaggine[testaY][testaX]==rossa:
            immaggine[corpo[0][0]][corpo[0][1]]=verde
            break
        elif immaggine[testaY][testaX]==verde:
            immaggine[corpo[0][0]][corpo[0][1]]=verde
            break
            
        else:
            immaggine[testaY][testaX]=verde
            corpo.append((testaY,testaX))
            corpo.pop(0)

        
    count= len(corpo)
    images.save(immaggine, out_img)
    return count

print("lunghezza serpente = ",generate_snake("./data/test.png", [0,0], "S S S S S  S S S S S S S S E S S S E E E E E E E E E E E E E E E E E E N E N N N N E S E E E N W W N W W W S S E N E S E E N W N W W W W W W W W W W N N N N W N E E S S S S E E N E E S S S S W N N W W W W N W W W W N W S S S S W S W S W N W N E N N N W W W W S S S S S W W N N N W W N W W W S S S S S E E E E E E E S S S S S SE SE SE SE SE SE SE SE NE NE S E E E E E E E E E E E E E E E E E E E NE NE NE NE NE S NW S SE SE SE SE SE SE SE SE NE NE S E E E E E E E E E E E E E E E E E E E NE NE NE NE NE S" , "./output/test.png"))#print("lunghezza serpente = ",generate_snake("./data/input_01.png", [1,28], "N N E E E E E E E E E E E NE NE NE NE NE NW NW NW NW NW NW NE NW NE NE NE NE E E SE N SW SW N S NE N NE W SW S NE NE S S NW SW N NE E W SW SW W W SE S S W N S S SW SW E S S W W S S W SE W W N SE E NW N N S SW S SE E NE E S S SE SE W SE W SE N S E SW NW W NE NE SW S S NW S NE E SE E S N E NW N S NE S N E E SW S S SE E E NW NW S S S E N S E E S W SW E S SE NW SE E S SW N N SW SW SW N SW SE NE E N SW N NW N SE W SE N N E N NW N SW NW W S NW NE SW NE NE NE S S W NE W NW S E NW SW S N S N W SW NW S W S SE S NW SE SE E N E W N S SW S SE NE NW W E N SW N SW S N S E S NE SW SW W E E S E W N SE S S W NE SW SW SW S S NW E SW S N SW SE SE SW SW NW E SE W E SE W E N SW N E SE SE N W S W S W SW S NE N SW SW S SW S SW NE S E SW S SW SW SW SE SW N S NE SW E SE SE NE NW S NE W SE W SW W W S SW W S N N S E E NE SE E S E E W E NW SE NW N S E W NW S E SE S NW NW S N S S SE SE NW W NE NW NE E SE NW S S N E E NE SW SE SE S SW E N S E NW NE S NW S NE N SW W NW SW W NE SW E NW NE N W E W NW E SE SW NW SE SE W NW E W SE SW E SW S N E S E S SE S S E W N NW N NE E NE NE S SW S NE W W NE NE E SE E NE SE E E N N S N NE W W S SE W SW S E W N SW N E W N S W NE S SW SE NW NW NW S W NW N N NW SW W S E S S S N SE NE W NW SW NE NW SE N SW NE S W NW NE NW NE S E NW S N NE W NE SE SE S E SE NW NE NE SW S S SW NW E SW SE S NE W E SW N SE W W E W SW SE SW W E SE SW E SW NE SE S SW N E E S NE NE NE NW SE SW E SE NE E E SE NW S S N SW S NW W NW NW S N SE S E N W NE W S S NE S NW S SW SE S S S S S SE S S S E W N NW N NE NE E SW N NW E S N N S NE SE NW E NW SW E SE SW NE NW NE N E E NW NW N S NE N W NW SE E S S SW SE NE NW E NE N E S N NW SE S S SW N SW NW SE S E SE NW W NE W SE SE S NE SE S E NW S S NE E SW SW E S NE SE SE E S S SW SW SE N E W N NW NW S N NE E E S NW NE NW N E NE S S W E S SW SW E SW NE W SE NW N", "./output/expected_end_01.png"))

#print("lunghezza serpente = ",generate_snake("./data/input_06.png", [28,1], "S S S S E S S S E E E E E E E E E E E E E E E E E E N E N N N N E S E E E N W W N W W W S S E N E S E E N W N W W W W W W W W W W N N N N W N E E S S S S E E N E E S S S S W N N W W W W N W W W W N W S S S S W S W S W N W N E N N N W W W W S S S S S W W N N N W W N W W W S S S S S E E E E E E E S S S S S SE SE SE SE SE SE SE SE NE NE S E E E E E E E E E E E E E E E E E E E NE NE NE NE NE S NW S SE SE SE SE SE SE SE SE NE NE S E E E E E E E E E E E E E E E E E E E NE NE NE NE NE S", "./output/output_end_06.png"))

