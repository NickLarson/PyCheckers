##Example: {1 : 1} would denote row 1, column 1
##Example 2: {{1 : 1}
class board():
    """initializing a board class..."""
    def __init__(self, size):
        self.board = {}
        for row in range(1,size+1):
            self.board[row] = {}                  ##Set the board to be full of dictionaries
            for column in range(1,size+1):
                self.board[row][column] = "EMPTY" ##Initialize to empty
    def getLocation(self, row, col):
        return self.board(row,col)
    
