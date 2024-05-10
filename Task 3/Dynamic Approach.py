def print_switch_state(switches):
    print("New Step" ":") 
    print("".join(map(str, switches[:-1])))

def min_moves(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    Memory_moves = [0] * (n + 1)
    switches = [1] * (n + 1)
    Memory_moves[1] = 1
    Memory_moves[2] = 2

    for i in range(3, n + 1):
        Memory_moves[i] = Memory_moves[i - 1] + 2 * Memory_moves[i - 2] + 1



    print("Repeat ", n - 2, " Switches Moves\n")  

    for i in range(0, n + 1):
        if i != 1:  
            switches[i] = 1 - switches[i]
     
    print_switch_state(switches)
            
            
    print("Repeat ", n - 2, "Switches Moves\n") 
    print("Repeat ", n - 1, "Switches Moves\n") 
    print("Minimum number of moves:", Memory_moves[n])


n = int(input("Enter the number of Security switches: "))
min_moves(n)

