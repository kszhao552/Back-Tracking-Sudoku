
class Board:
    def __init__(self):
        """creates a new board"""
        self.board = [[0 for i in range(9)]]*9
        self.board = [[0, 0, 0, 0, 3, 0, 9, 0, 0],
                      [0, 0, 3, 0, 8, 0, 0, 0, 7],
                      [6, 0, 0, 0, 0, 0, 4, 0, 0],
                      [0, 5, 8, 3, 6, 0, 0, 0, 0],
                      [0, 1, 0, 8, 9, 4, 0, 6, 0],
                      [0, 0, 0, 0, 2, 7, 8, 4, 0],
                      [0, 0, 9, 0, 0, 0, 0, 0, 8],
                      [7, 0, 0, 0, 4, 0, 6, 0, 0],
                      [0, 0, 5, 0, 1, 0, 0, 0, 0]]

    def __repr__(self):
        """prints out the current state of the sudoku board"""
        t = ''
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                t += str(self.board[x][y]) + ' '
            t += '\n'
        return t

    def checkCollumn(self, y):
        """checks the given current row to see if it is currently viable
        if it is, it reuturns true and otherwise, false"""
        used = []
        for x in range(len(self.board)):
            cur = self.board[x][y]
            if cur not in used:
                if cur!= 0:
                    used += [cur]
            else:
                return False
        return True

    def checkRow(self, x):
        """checks the given row to see if it is currently viable
        if it is, it reuturns true and otherwise, false"""
        used = []
        for y in range(len(self.board[0])):
            cur = self.board[x][y]
            if cur not in used:
                if cur !=0:
                    used += [cur]
            else:
                return False
        return True

    def checkBox(self, x, y):
        """checks the given row, starting at the top left, to see
        if it is currently viable.
        if it is, it reuturns true and otherwise, false"""
        used = []
        for i in range(3):
            for j in range(3):
                cur = self.board[x+i][y+j]
                if cur not in used:
                    if cur !=0:
                       used += [cur]
                else:
                    return False
        return True 

    def checkInput(self, x, y):
        """checks to see if the current input at a spot is viable.
        checks the input's collumn and row, and checks every box"""
        if self.checkCollumn(y) and self.checkRow(x):
            for i in range(3):
                for j in range(3):
                    if not self.checkBox(i*3, j*3):
                        return False
            return True
        return False
            
    def checkBoard(self):
            for x in range(3):
                for y in range(3):
                    if not self.checkBox(x*3, y*3):
                        return False
            for x in range(len(self.board)):
                for y in range(len(self.board[0])):
                    if not self.checkRow(x) and not self.checkCollumn(y):
                        return False
            return True
                    
def checkEmpty(grid):
    """given a grid, checks to see if there are any empty spots.
    if there is, then it returns true, and otherwise false"""
    for x in range(len(grid.board)):
        for y in range(len(grid.board[0])):
            if grid.board[x][y] == 0:
                return True
    return False

def findEmpty(grid):
    """finds where there is currently an empty spot in a grid
    returns the first 0 that it runs into"""
    for x in range(len(grid.board)):
        for y in range(len(grid.board[0])):
            if grid.board[x][y] == 0:
                return [x,y]

def solveSudoku(grid):
    """solves the sudoku board"""

    #if the board is not empty, then check to see if its solved
    #return True if it is
    if not findEmpty(grid):
        if grid.checkBoard():
            return True
        else:
            return False
    #finds the first empty position
    p = findEmpty(grid)
    #considers 1-9 and then places it into the empty spot
    for i in range(1, 10):
        grid.board[p[0]][p[1]] = i
        #if the input is viable, then it goes solves the new given board until its solved
        if grid.checkInput(p[0], p[1]):
            if solveSudoku(grid):
                return True
    #if there are no viable options for that spot, then it backtracks        
    grid.board[p[0]][p[1]] = 0
    return False

def main():
    b = Board()
    print(b)
    if solveSudoku(b):
        print(b)
    else:
        print("No solution")
        
if __name__== "__main__":
    main()


