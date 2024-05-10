import random

n = int(input("Enter number of hiding spots: "))
target_position = random.randint(1, n)

def find_target(hiding_spots): 
    if(n > 1):
        position = 2
    else:
        position = 1
    
    direction = 0
    spots = []
    for i in range(1, n+1):
        spots.append(i)
        
    while True:
        hit = shoot(position)
        if hit:
            break
        
        if position == n:
            continue
        else:
            if direction == 0 and position == 2:
                direction = 1
            elif direction == 0 and position == n-1:
                direction = -1
            elif position == 2 or position == n-1:
                direction = 0
            position += direction

            

def move_target():  #moving the target to the next position
    global target_position
    if(target_position == 1): 
        target_direction = 1
    elif(target_position == n):
        target_direction = -1
    else:
        target_direction = (-1)**random.randint(1, 2)
    target_position += target_direction

       

      
        
def shoot(position):
    global number_of_shots
    number_of_shots += 1
    print("Shooting position:", position)
    print("target position:", target_position)
    if position == target_position:
        print("\nTarget is shot!")
        print("\nnumber of shots: ", number_of_shots)
        return True
    else:
        move_target()
    
    

number_of_shots = 0
find_target(n)

