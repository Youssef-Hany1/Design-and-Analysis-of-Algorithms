import random

n = 6

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

def is_valid(x, y, board):
    if (x < 0) or (y < 0) or (x >= n) or (y >= n) or (board[y][x] != -1):
        return False
    return True

def print_board(board):
    for i in range(n):
        for j in range(n):
            print(str(board[i][j]).rjust(2), end=' ')
        print()

def neighbour(x, y, xx, yy):
    for i in range(n):
        if ((x + move_x[i]) == xx) and ((y + move_y[i]) == yy):
            return True
    return False

def findClosedTour():
    board = [[-1 for x in range(n)] for y in range(n)]
    sx = random.randint(0, n - 1)
    sy = random.randint(0, n - 1)
    board[sy][sx] = 0 # Mark first move.
    ret = None
    for i in range(1, n * n):
        ret = solveKTUtil(n, board, sx, sy, move_x, move_y, board[sy][sx], sx, sy)
        if ret == None:
            return False
    if not neighbour(ret[0], ret[1], sx, sy):
        return False
    print_board(board)
    return True

def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos, start_x, start_y):
    if pos == n*n:
        if is_valid(curr_x, curr_y, board) and neighbour(curr_x, curr_y, start_x, start_y):
            board[curr_y][curr_x] = pos
            return (curr_x, curr_y)
        else:
            return None

    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_valid(new_x, new_y, board):
            board[new_y][new_x] = pos
            if solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1, start_x, start_y):
                return (new_x, new_y)
            board[new_y][new_x] = -1
    return None

if __name__ == "__main__":
    findClosedTour()

