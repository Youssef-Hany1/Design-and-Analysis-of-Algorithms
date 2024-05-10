GRID_SIZE = 8  # Size of the grid
MISSING_X, MISSING_Y, TROMINO_NO = 2, 3, 0  # Coordinates of the missing tile and current tromino number
Board = [[0] * 128 for _ in range(128)]  # 2D array representing the board
N_TROMINOS = (GRID_SIZE * GRID_SIZE) // 3  # Number of trominos needed to fill the board
MEMOIZATION = [[[[ -1 for _ in range(129)] for _ in range(129)] for _ in range(129)] for _ in range(129)]  # Memoization table for dynamic programming


# placeing a tromino at the given coordinates
def coordinate(x1, y1, x2, y2, x3, y3):
    global TROMINO_NO
    TROMINO_NO += 1 
    # Assign the same tromino number to the given coordinates
    Board[x1][y1] = TROMINO_NO
    Board[x2][y2] = TROMINO_NO
    Board[x3][y3] = TROMINO_NO


#recursively place trominos on the board
def place(n, x, y, MISSING_X, MISSING_Y):
    # Check if result is already memoized
    if MEMOIZATION[n][x][y][MISSING_X] != -1:
        return MEMOIZATION[n][x][y][MISSING_X]
    row, column = 0, 0
    # Base case: 2x2 grid
    if n == 2:
        global TROMINO_NO
        TROMINO_NO += 1
        # Place the tromino
        for i in range(n):
            for j in range(n):
                if Board[x + i][y + j] == 0:
                    Board[x + i][y + j] = TROMINO_NO
        return 0

    # Find the position of the already placed tromino
    for i in range(x, x + n):
        for j in range(y, y + n):
            if Board[i][j] != 0:
                row, column = i, j

    # Recursive calls to place trominos
    return dp(x, y, n, MISSING_X, MISSING_Y, row, column)


# Function for dynamic programming to place trominos
def dp(x, y, n, MISSING_X, MISSING_Y, row, column):
    # Calculate the coordinates of quadrants
    x_quad, y_quad = x + n // 2, y + n // 2
    y_L, x_L = y + (n // 2) - 1, x + (n // 2) - 1

    # Based on the position of the already placed tromino, place the missing tromino
    if row < x_quad and column < y_quad:
        coordinate(x_quad, y_L, x_quad, y_quad, x_L, y_quad)
    elif row < x_quad and column >= y_quad:
        coordinate(x_quad, y_L, x_quad, y_quad, x_L, y_L)
    elif row >= x_quad and column < y_quad:
        coordinate(x_L, y_quad, x_quad, y_quad, x_L, y_L)
    elif row >= x_quad and column >= y_quad:
        coordinate(x_L, y_quad, x_quad, y_L, x_L, y_L)

    # Recursive calls to place trominos
    result = 0
    result += place(n // 2, x, y_quad, MISSING_X, MISSING_Y)
    result += place(n // 2, x, y, MISSING_X, MISSING_Y)
    result += place(n // 2, x_quad, y, MISSING_X, MISSING_Y)
    result += place(n // 2, x_quad, y_quad, MISSING_X, MISSING_Y)

    MEMOIZATION[n][x][y][MISSING_X] = result  #dp=>top down
    return result


# class representing a tromino
class Tromino:
    def __init__(self):
        self.num = 0  # Tromino number
        self.color = 0  # Color assigned to the tromino
        self.neighbors = []  # Neighboring trominos


trominos = [Tromino() for _ in range(N_TROMINOS)]  # Array of trominos


def color_tromino():
    
    for i in range(N_TROMINOS):
        trominos[i].num = i + 1
        trominos[i].color = 0
    # Assign neighboring trominos
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            num = Board[i][j]
            if num != -1:
                index = num - 1
                tromino = trominos[index]

                if i > 0 and Board[i - 1][j] != -1:
                    tromino.neighbors.append(Board[i - 1][j] - 1)

                if j > 0 and Board[i][j - 1] != -1:
                    tromino.neighbors.append(Board[i][j - 1] - 1)
                if i < GRID_SIZE - 1 and Board[i + 1][j] != -1:
                    tromino.neighbors.append(Board[i + 1][j] - 1)
                if j < GRID_SIZE - 1 and Board[i][j + 1] != -1:
                    tromino.neighbors.append(Board[i][j + 1] - 1)


# Function to check if a color can be assigned to a tromino
def color_checker(tromino, color):
    for neighbor in tromino.neighbors:
        if trominos[neighbor].color == color:
            return False
    return True



def isColored(index):
    if index == N_TROMINOS:
        return True  
    tromino = trominos[index]
    
    for color in range(1, N_TROMINOS + 1):
        if color_checker(tromino, color):
            tromino.color = color
            if isColored(index + 1):
                return True  
            tromino.color = 0  
    return False  



def printme():
    coloring = [0] * (N_TROMINOS + 1)
    print("Colored trominoes : ")
    for i in range(GRID_SIZE):
        # Print horizontal line before each row
        print("+", end="")
        for _ in range(GRID_SIZE):
            print("-------+", end="")
        print()

        # Print cells of the board with numbers or colors
        for j in range(GRID_SIZE):
            num = Board[i][j]
            print("| ", end="")
            if num != -1:
                color = trominos[num - 1].color
                if color == 1:
                    print("G ", end="")
                elif color == 2:
                    print("B ", end="")
                else:
                    print("R ", end="")
                coloring[color] = num
            else:
                print("X ", end="")
        print("|")

    # Print horizontal line after the last row
    print("+", end="")
    for _ in range(GRID_SIZE):
        print("-------+", end="")
    print()

    print("Numbered trominoes : ")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(f"{Board[i][j]:7}", end=" ")
        print()


if __name__ == "__main__":
    if GRID_SIZE > 0 and (GRID_SIZE & (GRID_SIZE - 1)) != 0:
        print("Invalid  size")
    else:
        # Place missing tile
        Board[MISSING_X][MISSING_Y] = -1
        place(GRID_SIZE, 0, 0, MISSING_X, MISSING_Y)
        color_tromino()
       
        if isColored(0):
            print("success:")
            printme()
        else:
            print("faild")

