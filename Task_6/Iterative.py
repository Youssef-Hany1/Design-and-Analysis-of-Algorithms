def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def find_knights(board, color):
    return [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == color]

def valid_moves(x, y, board):
    moves = [
        (x + 2, y + 1), (x + 2, y - 1),
        (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x + 1, y - 2),
        (x - 1, y + 2), (x - 1, y - 2)
    ]
    return [(nx, ny) for nx, ny in moves if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == '.']

def move_knight(board, x, y, nx, ny):
    board[nx][ny], board[x][y] = board[x][y], '.'

def exchange_knights(board):
    steps = 0
    while True:
        white_knights = find_knights(board, 'W')
        black_knights = find_knights(board, 'B')
        
        # Iterate through white knights and their valid moves
        for x, y in white_knights:
            for nx, ny in valid_moves(x, y, board):
                move_knight(board, x, y, nx, ny)
                steps += 1
                print_board(board)
                # Check if the board has reached the desired state
                if sorted(find_knights(board, 'W')) == [(0, 0), (0, 1), (0, 2)] and sorted(find_knights(board, 'B')) == [(3, 0), (3, 1), (3, 2)]:
                    return steps
        
        # Iterate through black knights and their valid moves
        for x, y in black_knights:
            for nx, ny in valid_moves(x, y, board):
                move_knight(board, x, y, nx, ny)
                steps += 1
                print_board(board)
                # Check if the board has reached the desired state
                if sorted(find_knights(board, 'W')) == [(0, 0), (0, 1), (0, 2)] and sorted(find_knights(board, 'B')) == [(3, 0), (3, 1), (3, 2)]:
                    return steps

# Initial board setup
board = [
    ['B', 'B', 'B'],
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['W', 'W', 'W']
]

# Run the algorithm
steps = exchange_knights(board)
print(f"Total steps taken: {int(steps)}")