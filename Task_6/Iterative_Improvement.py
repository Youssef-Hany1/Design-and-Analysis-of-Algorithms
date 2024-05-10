import copy

# Define the initial state
initial_state = [
    ['W', 'W', 'W'],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    ['B', 'B', 'B']
]

# Define the goal state
goal_state = [
    ['B', 'B', 'B'],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    ['W', 'W', 'W']
]

# Define a heuristic function to evaluate the distance between two states
def heuristic(state):
    # Calculate the number of knights in the correct position
    score = 0
    for i in range(4):
        for j in range(3):
            if state[i][j] == goal_state[i][j]:
                score += 1
    return score

# Define a function to generate possible moves
def generate_moves(state):
    moves = []
    for i in range(4):
        for j in range(3):
            # Check if the knight at position (i, j) can be moved
            if state[i][j] == 'W':
                # Check possible moves for a white knight
                if i > 0 and state[i - 1][j] == ' ':
                    # Move up
                    new_state = copy.deepcopy(state)
                    new_state[i][j] = ' '
                    new_state[i - 1][j] = 'W'
                    moves.append(new_state)
                # Add more possible moves based on knight's movement pattern (e.g., left, right, etc.)
            elif state[i][j] == 'B':
                # Check possible moves for a black knight
                # Implement similar logic for black knights
                pass
    return moves if moves else [state]  # Return current state if no moves are available

# Define the iterative improvement algorithm
def iterative_improvement():
    current_state = initial_state
    iteration = 0
    while True:
        iteration += 1
        print("Iteration:", iteration)
        print("Current state:")
        for row in current_state:
            print(' '.join(row))
        
        # Check if the current state matches the goal state
        if current_state == goal_state:
            print("Goal state reached!")
            break
        
        # Generate possible moves
        moves = generate_moves(current_state)
        
        # Ensure that moves list is not empty
        if moves:
            # Evaluate possible moves and select the best move based on the heuristic function
            best_move = None
            best_score = -1
            for move in moves:
                score = heuristic(move)
                if score > best_score:
                    best_move = move
                    best_score = score
        
            # Apply the best move
            current_state = best_move
        else:
            print("No valid moves available.")
            break

# Run the iterative improvement algorithm
iterative_improvement()