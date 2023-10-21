import images
def check_diagonal_intruction(matriceImmagine,snake_body_positions,checkPos,limit,nextPos): 
    forbidden_one=check_limit([nextPos[0],nextPos[1]+checkPos[1]*-1],limit) #checkPos[1]*-1
    forbidden_two=check_limit([nextPos[0]+checkPos[0]*-1,nextPos[1]],limit) #checkPos[0]*-1
    cnt = 0
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
        if not calculate_input(matriceImmagine,snake_body_positions,limit,DizComandi[direction])[1]:
            break
    images.save(matriceImmagine,out_img)
    return len(snake_body_positions)
def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    return get_commands(commands.split(),images.load(start_img),position,out_img)