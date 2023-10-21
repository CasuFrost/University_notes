import imagesDebug as images
import time
def check_diagonal_intruction(matriceImmagine,snake_body_positions,checkPos,limit,nextPos): 
    forbidden_one=check_limit([nextPos[0],nextPos[1]+checkPos[1]*-1],limit) #checkPos[1]*-1
    forbidden_two=check_limit([nextPos[0]+checkPos[0]*-1,nextPos[1]],limit) #checkPos[0]*-1
    cnt =0
    if matriceImmagine[forbidden_one[0]][forbidden_one[1]]==(0,255,0):
        cnt+=1
    if matriceImmagine[forbidden_two[0]][forbidden_two[1]]==(0,255,0) and cnt==1:
        return False
    return True
def calculate_input(matriceImmagine,snake_body_positions,limit,checkPos):
    nextPos=[snake_body_positions[0][0],snake_body_positions[0][1]]
    nextPos[0]+=checkPos[0]
    nextPos[1]+=checkPos[1]  
    nextPos=check_limit(nextPos,limit)  
    if matriceImmagine[nextPos[0]][nextPos[1]]!=(255,0,0): #check obstacles   
        if matriceImmagine[nextPos[0]][nextPos[1]]!=(0,255,0): #check cross intruction
            if check_diagonal_intruction(matriceImmagine,snake_body_positions,checkPos,limit,nextPos):#check diagonal intruction
                snake_body_positions=ricalcolo_posizioni_serpente(snake_body_positions,nextPos,matriceImmagine)
            else:            
                return snake_body_positions,False
        else:      
            return snake_body_positions,False
    else:
        return snake_body_positions,False
    return snake_body_positions,True

def check_limit(nextPos,limit):
    nextPos[1]%=limit["y"]
    nextPos[0]%=limit["x"]
    return nextPos

def ricalcolo_posizioni_serpente(snake_body_positions,newPos,matriceImmagine):
    snake_body_positions.insert(0,newPos)
    if matriceImmagine[newPos[0]][newPos[1]]==(255,128,0):
        matriceImmagine[newPos[0]][newPos[1]]=(0,255,0)
        return snake_body_positions
    else:
        matriceImmagine[newPos[0]][newPos[1]]=(0,255,0)
        matriceImmagine[snake_body_positions[-1][0]][snake_body_positions[-1][1]]=(128,128,128)
        snake_body_positions.pop(-1)
    return snake_body_positions
def get_commands(commands,matriceImmagine,position,out_img):
    snake_body_positions =[position[::-1]]
    limit = {'x':len(matriceImmagine),'y':len(matriceImmagine[0])}
    DizComandi = {'W':(0,-1),'E':(0,1),'N':(-1,0),'S':(1,0),'NW':(-1,-1),'NE':(-1,1),'SW':(1,-1),'SE':(1,1)}
    for direction in commands:  
        time.sleep(0.05)
        images.save(matriceImmagine,out_img)
        images.visd(matriceImmagine)
        try:
            if not calculate_input(matriceImmagine,snake_body_positions,limit,DizComandi[direction])[1]:
                break
        except Exception:
            pass
    
    return len(snake_body_positions)
def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    return get_commands(commands.split(),images.load(start_img),position,out_img)
    
    
start = time.time()

print("lunghezza serpente = ",generate_snake("./data/test.png", [0,0], "S S  S S   S  S S   S S S S  S S   S S S S S S E E E E E  E E E E E  E E NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW NW  NW NW NW NW NW NW NW NW NW  NW NW NW NW NW NW NW NW NW  NW NW NW NW NW NW NW NW NW " , "./output/test.png"))#print("lunghezza serpente = ",generate_snake("./data/input_01.png", [1,28], "N N E E E E E E E E E E E NE NE NE NE NE NW NW NW NW NW NW NE NW NE NE NE NE E E SE N SW SW N S NE N NE W SW S NE NE S S NW SW N NE E W SW SW W W SE S S W N S S SW SW E S S W W S S W SE W W N SE E NW N N S SW S SE E NE E S S SE SE W SE W SE N S E SW NW W NE NE SW S S NW S NE E SE E S N E NW N S NE S N E E SW S S SE E E NW NW S S S E N S E E S W SW E S SE NW SE E S SW N N SW SW SW N SW SE NE E N SW N NW N SE W SE N N E N NW N SW NW W S NW NE SW NE NE NE S S W NE W NW S E NW SW S N S N W SW NW S W S SE S NW SE SE E N E W N S SW S SE NE NW W E N SW N SW S N S E S NE SW SW W E E S E W N SE S S W NE SW SW SW S S NW E SW S N SW SE SE SW SW NW E SE W E SE W E N SW N E SE SE N W S W S W SW S NE N SW SW S SW S SW NE S E SW S SW SW SW SE SW N S NE SW E SE SE NE NW S NE W SE W SW W W S SW W S N N S E E NE SE E S E E W E NW SE NW N S E W NW S E SE S NW NW S N S S SE SE NW W NE NW NE E SE NW S S N E E NE SW SE SE S SW E N S E NW NE S NW S NE N SW W NW SW W NE SW E NW NE N W E W NW E SE SW NW SE SE W NW E W SE SW E SW S N E S E S SE S S E W N NW N NE E NE NE S SW S NE W W NE NE E SE E NE SE E E N N S N NE W W S SE W SW S E W N SW N E W N S W NE S SW SE NW NW NW S W NW N N NW SW W S E S S S N SE NE W NW SW NE NW SE N SW NE S W NW NE NW NE S E NW S N NE W NE SE SE S E SE NW NE NE SW S S SW NW E SW SE S NE W E SW N SE W W E W SW SE SW W E SE SW E SW NE SE S SW N E E S NE NE NE NW SE SW E SE NE E E SE NW S S N SW S NW W NW NW S N SE S E N W NE W S S NE S NW S SW SE S S S S S SE S S S E W N NW N NE NE E SW N NW E S N N S NE SE NW E NW SW E SE SW NE NW NE N E E NW NW N S NE N W NW SE E S S SW SE NE NW E NE N E S N NW SE S S SW N SW NW SE S E SE NW W NE W SE SE S NE SE S E NW S S NE E SW SW E S NE SE SE E S S SW SW SE N E W N NW NW S N NE E E S NW NE NW N E NE S S W E S SW SW E SW NE W SE NW N", "./output/expected_end_01.png"))

#generate_snake("./data/input_05.png", [32, 94],"NE NE NE NE NE NE  NE NE NE  NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE W W W W W W W S S S S S S S E S S N N N SW SW S W S N E S E W S N NW S SE W N S E SW SW S W E NW S S E E E SW S SE E NW N S NW S E NW SW E SE N SW NW NE S NE NE NE E N S S W E NE S S W SE NE SE E N SE SE SW S E S S NW E NW S S NE N NE NE W W SW NW N SW S NE S W S NE NW NW NW SW SE S SW NE S S N E E E NE S NE W E SW NW SW S NE SE W SW E NE NE NE S NW S NW S W SW SW N SE E SE NE S SE W SW S W SW N W NE S W W SE NE S E S N SW SW S E N SE SE S SW S NW SW E NW E E W S N S NW S W E S SE S N E E N SW SE E W S E S SW SE E NW W NW W N SW SW S E N SW NW SW W E NW E N E S N S SW E E S E NW NE NE SE S N S NE N NW W S S S SW E W NE W E S SE E N NE NE W SE SW NW SW E S E N SE E S NE S E NW S SW NW E S NW S SE NW NW S S S S SE N SE SE NE SE NE N SE NW NW NW NE SE NE S S N N S SW S W W E NE SW W N NE NW NW S S E SE E N E SW SE S NE N NW E E NE NE S S S NW W SW W S S N S E E S N S SE S W W SW SW W SW NW S SE E SE W NE W W S E NW SW N NW SW S NE SW SW SE S SW N W SW NE W NE NE NE NW S S S SW NW S N W S W NE S S S S W S","./output/output_end_05.png")
#print(a)
#print("lunghezza serpente = ",generate_snake("./data/input_06.png", [28,1], "S S S S E S S S E E E E E E E E E E E E E E E E E E N E N N N N E S E E E N W W N W W W S S E N E S E E N W N W W W W W W W W W W N N N N W N E E S S S S E E N E E S S S S W N N W W W W N W W W W N W S S S S W S W S W N W N E N N N W W W W S S S S S W W N N N W W N W W W S S S S S E E E E E E E S S S S S SE SE SE SE SE SE SE SE NE NE S E E E E E E E E E E E E E E E E E E E NE NE NE NE NE S NW S SE SE SE SE SE SE SE SE NE NE S E E E E E E E E E E E E E E E E E E E NE NE NE NE NE S", "./output/output_end_06.png"))
print(time.time()-start)