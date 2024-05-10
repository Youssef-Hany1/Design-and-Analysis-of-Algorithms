import random

n = int(input("Enter number of hiding spots: "))
target_position = random.randint(1, n)

def find_target(hiding_spots): 
    if(n > 1):
        position = 2
    else:
        position = 1
    
    direction = 1
    spots = []
    for i in range(1, n+1):
        spots.append(i)

    path = []
    dynamic(position, path)


def dynamic(position, path):
    hit = shoot(position, True)
    if hit:
        return
    
    path.append(position)
    if position == n-1 or position == n:
        print("\n repeating the previous shots in reverse\n")
        memory(path)
        return
    
    return dynamic(position + 1, path)

def memory(path):
    for i in range(-1, -n, -1):
        position = path[i]
        hit = shoot(position, False)
        if hit:
            return
        

def move_target():  #moving the target to the next position
    global target_position
    if(target_position == 1): 
        target_direction = 1
    elif(target_position == n):
        target_direction = -1
    else:
        target_direction = (-1)**random.randint(1, 2)
    target_position += target_direction

       

      
        
def shoot(position, bool):
    global number_of_shots
    number_of_shots += 1
    if(bool):
        print("Shooting position:", position)
    if position == target_position:
        print("\nTarget is shot at position", position)
        print("\nnumber of shots: ", number_of_shots)
        return True
    else:
        move_target()

    
    
    

number_of_shots = 0
find_target(n)

