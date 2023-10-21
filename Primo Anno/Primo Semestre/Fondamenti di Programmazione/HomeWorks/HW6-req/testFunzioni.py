

def update_position(snake_body,command,grey_positions,Orange_positions):
    newPos=snake_body[0].copy()
    newSnakeBody = []
    validCommand=False
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
        
    if validCommand:
        newSnakeBody.append(newPos)    
        for i in range(len(snake_body)):
            if i!=len(snake_body)-1:     
                newSnakeBody.append(snake_body[i])
            else:
                grey_positions.append(snake_body[i])
            for orange in Orange_positions:
                if snake_body[i]==orange:
                    Orange_positions.remove(orange) 
                    last = grey_positions[len(grey_positions)-1]
                    snake_body.append(last)
                    grey_positions.remove(grey_positions[len(grey_positions)-1])
        return newSnakeBody
    return snake_body
        
def get_commands(commands,snake_body,grey_positions,Orange_positions):
    for i in commands:
        snake_body=update_position(snake_body,i,grey_positions,Orange_positions)
    return snake_body  


def get_orange_pos(immagineLista,positions):
    for i in range(len(immagineLista)):
        for j in range(len(immagineLista[i])):
            if immagineLista[i][j] == (255,128,0):
                positions.append([i,j])
    return positions
                


grey_positions=[]   
Orange_positions=[[2,1],[2,3]]

snake_body = [[0,0],[0,1],[0,2]]
#print(snake_body)
commands = "S S E E E E W S"
newPos = get_commands(commands,snake_body,grey_positions,Orange_positions)
print(newPos)
print(grey_positions)
print(Orange_positions)

