import random

n = 3
call_count = 0

# randomize position of missing square
def missing_square(board):
    n = len(board)
    row = random.randint(0, n - 1)
    col = random.randint(0, n - 1)
    board[row][col] = 'X '
    return board

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def search(arr, key):
    for row in arr:
        if key in row:
            return True
    return False



# called for the base case
def fill(board):
    global call_count

    for index, row in enumerate(board):
        for col, cell in enumerate(row):
            if cell == 'C ':
                if call_count % 4 == 0 or call_count % 4 == 3:
                    board[index][col] = 'R '
                else:
                    board[index][col] = 'G '

    call_count += 1



def color_corner(board, missing, mid_index):
    if missing == 1:
        board[mid_index][mid_index+1] = 'B '
        board[mid_index+1][mid_index] = 'B '
        board[mid_index+1][mid_index+1] = 'B '
    elif missing == 2:
        board[mid_index][mid_index] = 'B '
        board[mid_index+1][mid_index] = 'B '
        board[mid_index+1][mid_index+1] = 'B '
    elif missing == 3:
        board[mid_index][mid_index] = 'B '
        board[mid_index][mid_index+1] = 'B '
        board[mid_index+1][mid_index+1] = 'B '
    elif missing == 4:
        board[mid_index][mid_index] = 'B '
        board[mid_index][mid_index + 1] = 'B '
        board[mid_index + 1][mid_index] = 'B '


def divide(board, n):
    if n == 1:
        fill(board)

    else:
        edge = 2 ** n
        mid = edge // 2

        q1 = [[board[i][j] for j in range(mid)] for i in range(mid)]
        q2 = [[board[i][j] for j in range(mid, edge)] for i in range(mid)]
        q3 = [[board[i][j] for j in range(mid)] for i in range(mid, edge)]
        q4 = [[board[i][j] for j in range(mid, edge)] for i in range(mid, edge)]

        missing = -1
        if search(q1, 'X ') or search(q1, 'B '):
            missing = 1
        elif search(q2, 'X ') or search(q2, 'B '):
            missing = 2
        elif search(q3, 'X ') or search(q3, 'B '):
            missing = 3
        elif search(q4, 'X ') or search(q4, 'B '):
            missing = 4

        color_corner(board, missing, mid-1)

        q1 = [[board[i][j] for j in range(mid)] for i in range(mid)]
        q2 = [[board[i][j] for j in range(mid, edge)] for i in range(mid)]
        q3 = [[board[i][j] for j in range(mid)] for i in range(mid, edge)]
        q4 = [[board[i][j] for j in range(mid, edge)] for i in range(mid, edge)]

        divide(q1, n-1)
        divide(q2, n-1)
        divide(q3, n-1)
        divide(q4, n-1)


        # merge the quarters to the original board
        for i in range(mid):
            for j in range(mid):
                board[i][j] = q1[i][j]
                board[i][j + mid] = q2[i][j]
                board[i + mid][j] = q3[i][j]
                board[i + mid][j + mid] = q4[i][j]



# the board size is edge * edge
edge = 2 ** n

# create a board with missing square
board = missing_square( [['C ' for _ in range(edge)] for _ in range(edge)] )

print_board(board)


print("\nTiled Board:")
divide(board, n)
print_board(board)