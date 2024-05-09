import random 

'''each cell has a position (x,y)'''
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
n = 8

'''L movement ------> take cx[0]and cy[0]
will use it later in code'''
cx = [1, 1, 2, 2, -1, -1, -2, -2]
cy = [2, -2, 1, -1, 2, -2, 1, -1]

'''check if cell is empty and within the 8*8 board'''
def is_valid(x, y, board):
    if (x < 0) or (y < 0) or (x >= n) or (y >= n) or (board[y][x] != -1):
        return False
    return True

"""Returns the number of empty squares adjacent to (x, y)"""
def numberValidSquares(board, x, y):
    count = 0
    for i in range(n):
        if is_valid(x + cx[i], y + cy[i], board):
            count += 1
    return count

'''The nextMove function implements Warnsdorff's heuristic. 
It iterates through all adjacent cells of the current cell, starting from a random adjacent cell.
It selects the next cell based on the one with the minimum number of valid squares among the unvisited cells. 
If no valid next move is found, it returns None. 
Otherwise, it updates the current cell's coordinates and marks the next move on the board.'''

def nextMove(board, cell, pos):
    min_deg_idx = -1
    min_deg = n + 1
    nx = 0
    ny = 0

#Find the adjacent with minimum degree
    start = random.randint(0, 1000) % n
    for count in range(n):
        i = (start + count) % n
        nx = cell.x + cx[i]
        ny = cell.y + cy[i]
        c = numberValidSquares(board, nx, ny)
        if is_valid(nx, ny, board) and c < min_deg:
            min_deg_idx = i
            min_deg = c 

    # IF we could not find a next cell
    if min_deg_idx == -1:
        return None
    
    # Store coordinates of next point
    nx = cell.x + cx[min_deg_idx]
    ny = cell.y + cy[min_deg_idx]
    
    # Mark next move
    board[ny][nx] = pos + 1

    # Update next point
    cell.x = nx
    cell.y = ny
    return cell
def print_board(board):
    for i in range(n):
        for j in range(n):
            print(str(board[i][j]).rjust(2), end=' ')
        print()
def neighbour(x, y, xx, yy):
    for i in range(n):
        if ((x + cx[i]) == xx) and ((y + cy[i]) == yy):
            return True
    return False
def findClosedTour():

    # Filling up the chessboard matrix with -1's
    board = [[-1 for x in range(n)] for y in range(n)]
    
    # initial position
    sx = random.randint(0, n - 1)
    sy = random.randint(0, n - 1)

    # Current points are same as initial points
    cell = Cell(sx, sy)
    board[cell.y][cell.x] = 1 # Mark first move.

    # Keep picking next points using Warnsdorff's heuristic
    ret = None
    for i in range(n * n - 1):
        ret = nextMove(board, cell, i)
        if ret == None:
            return False
        
    # Check if tour is closed (Can end at starting point)
    if not neighbour(ret.x, ret.y, sx, sy):
        return False
    print_board(board)
    return True
if __name__ == '__main__':
    while not findClosedTour():
        pass
