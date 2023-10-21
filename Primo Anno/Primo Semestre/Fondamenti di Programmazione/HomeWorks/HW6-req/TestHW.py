import images

def check_collision(snake_body,command,grey_positions):
    if command=="N":   
        nextPos = [snake_body[0][0]-1,snake_body[0][1]]
        if nextPos in snake_body and (nextPos!=snake_body[-1]):
            grey_positions.append(snake_body[-1])
            snake_body.pop(-1)
            return True
    if command=="S":   
        nextPos = [snake_body[0][0]+1,snake_body[0][1]]
        if nextPos in snake_body and (nextPos!=snake_body[-1]):
            grey_positions.append(snake_body[-1])
            snake_body.pop(-1)
            print("intruppo")
            return True
    if command=="E":   
        nextPos = [snake_body[0][0],snake_body[0][1]+1]
        if nextPos in snake_body and (nextPos!=snake_body[-1]):
            grey_positions.append(snake_body[-1])
            snake_body.pop(-1)
            return True
    if command=="W":   
        nextPos = [snake_body[0][0],snake_body[0][1]-1]
        if nextPos in snake_body and (nextPos!=snake_body[-1]):
            grey_positions.append(snake_body[-1])
            snake_body.pop(-1)
            return True
    if command=="SW":   
        nextPos = [snake_body[0][0]+1,snake_body[0][1]-1]
        nextPos1 = [snake_body[0][0],snake_body[0][1]-1]
        nextPos2=[snake_body[0][0]+1,snake_body[0][1]]
        if nextPos in snake_body or (nextPos1 in snake_body and nextPos2 in snake_body) :
            grey_positions.append(snake_body[-1])
            snake_body.pop(-1)
            print("intruppo")
            return True
    if command=="SE":   
        nextPos = [snake_body[0][0]+1,snake_body[0][1]+1]
        nextPos1 = [snake_body[0][0],snake_body[0][1]+1]
        nextPos2 = [snake_body[0][0]+1,snake_body[0][1]]
        if nextPos in snake_body or (nextPos1 in snake_body and nextPos2 in snake_body):
            grey_positions.append(snake_body[-1])
            snake_body.pop(-1)
            print("intruppo")
            return True
    if command=="NW":   
        
        nextPos = [snake_body[0][0]-1,snake_body[0][1]-1]
        nextPos1 = [snake_body[0][0],snake_body[0][1]-1]
        nextPos2 = [snake_body[0][0]-1,snake_body[0][1]]
        if nextPos in snake_body or (nextPos1 in snake_body and nextPos2 in snake_body):
            grey_positions.append(snake_body[-1])
            snake_body.pop(-1)
          
            return True
    if command=="NE":   
        nextPos = [snake_body[0][0]-1,snake_body[0][1]+1]
        nextPos1 = [snake_body[0][0]-1,snake_body[0][1]]
        nextPos2 = [snake_body[0][0],snake_body[0][1]+1]
        if nextPos in snake_body or (nextPos1 in snake_body and nextPos2 in snake_body):
            grey_positions.append(snake_body[-1])
            snake_body.pop(-1)
            
            return True
def update_position(snake_body,command,grey_positions,Orange_positions,Red_Positions,getHitted,size,intruppato):
    newPos=snake_body[0].copy()
    newSnakeBody = []
    validCommand=False
    
    if check_collision(snake_body, command,grey_positions):
        intruppato[0]=True
    
    if "N" in command:
        newPos[0]-=1
        validCommand=True
    if "S" in command:
        newPos[0]+=1
        validCommand=True
    if "W" in command:
        newPos[1]-=1
        validCommand=True
    if "E" in command:
        newPos[1]+=1
        validCommand=True
        
    if newPos[0]<0:
         #Uscito verticalmente
         newPos[0]=size[1]-1

    if newPos[1]<0:
         #Uscito verticalmente
         newPos[1]=size[0]-1   
         
    if newPos[0]>size[1]-1:
        #Uscito verticalmente
        newPos[0]=0
    
    if newPos[1]>size[0]-1:
        #Uscito lateralmente
        newPos[1]=0
        
    
    if validCommand and not intruppato[0]:
        
        
        newSnakeBody.append(newPos)    
          
        
        for i in range(len(snake_body)):
            if i!=len(snake_body)-1:     
                newSnakeBody.append(snake_body[i])  
            else:
                grey_positions.append(snake_body[i])
          
        for i in range(len(snake_body)):
            for orange in Orange_positions:
                if newSnakeBody[i]==orange:
                    Orange_positions.remove(orange) 
                    last = grey_positions[len(grey_positions)-1]
                    newSnakeBody.append(last)
                    grey_positions.remove(grey_positions[len(grey_positions)-1])
            for red in Red_Positions:
                if newSnakeBody[i]==red:
                    getHitted[0]=True
                    return newSnakeBody 
       # a=[]
       # for i in newSnakeBody:
            #if i not in a:
            #    a.append(i)
           # else:
                #newSnakeBody.pop(0)
                #intruppato[0]=True
                #return newSnakeBody
            
        return newSnakeBody
    
    return snake_body

def check_duplicates(newSnakeBody):
    listaDaRiempire=[]
    for i in newSnakeBody:
        if i not in listaDaRiempire:
            listaDaRiempire.append(i)
        else:
            return True
    return False
    
        
def get_commands(commands,snake_body,grey_positions,Orange_positions,Red_Positions,getHitted,size,intruppato):
    commands = commands.split()
    for i in commands:
        if intruppato[0]==True:  
            snake_body.append(snake_body[0])
            return snake_body
        if getHitted[0]==True:
            Red_Positions.append(snake_body[0])
            return snake_body
        snake_body=update_position(snake_body,i,grey_positions,Orange_positions,Red_Positions,getHitted,size,intruppato)
    return snake_body  


def get_color_position(immagineLista,positions,color):
    for i in range(len(immagineLista)):
        for j in range(len(immagineLista[i])):
            if immagineLista[i][j] == color:
                positions.append([i,j])
    return positions


def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    
    getHitted=[False]
    intruppato=[False]
    immagineLista = images.load(start_img)
    size = [len(immagineLista[0]),len(immagineLista),]
    #print(size)
    grey_positions=[]
    Orange_positions=[]
    Orange_positions=get_color_position(immagineLista,Orange_positions,(255,128,0))
    Red_Positions=[]
    Red_Positions=get_color_position(immagineLista,Red_Positions,(255,0,0))
    
    snake_body=[position[::-1]]
    
    snake_body=get_commands(commands,snake_body,grey_positions,Orange_positions,Red_Positions,getHitted,size,intruppato)
    
    
    for i in range(len(immagineLista)):
        for j in range(len(immagineLista[i])):
            
                    
            for k in grey_positions:
                if k==[i,j]:
                    immagineLista[i][j]=(128,128,128)  
            for k in snake_body:
                if k==[i,j]:
                    immagineLista[i][j]=(0,255,0)   
            for k in Red_Positions:
                if k==[i,j]:
                    immagineLista[i][j]=(255,0,0)  
            
              
    images.save(immagineLista,out_img)
    return len(snake_body)

print("lunghezza serpente = ",generate_snake("./data/test.png", [0,0], "S S S S S S S E E E E E E E E N W   W S S S", "./output/test.png"))
