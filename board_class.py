class board():
    """
    The board class is a dictionary of dictionaries.
    This allows us to access the array in minimal time, and also
    allows us to keep it in order and good to go
    """
    def __init__(self, size):
        self.board = {}
        for row in range(1,size+1):
            self.board[row] = {}                  ##Set the board to be full of dictionaries
            for column in range(1,size+1):
                self.board[row][column] = "EMPTY" ##Initialize to empty
                
    def getLocation(self, row, col):
        return self.board(row,col)
        
    def setLocation(self, row, col, piece):
        if self.board[row][col] == "EMPTY":
            self.board[row][col] = piece
            return 0
        else:
            print "bad move"
            return -1
