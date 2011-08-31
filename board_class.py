class board():
    """
    The board class is a dictionary of dictionaries.
    This allows us to access the array in minimal time, and also
    allows us to keep it in order and good to go
    """
    def __init__(self, size):
        self.board = {}
        self.sizes = size
        for row in range(1,size+1):
            self.board[row] = {}                  ##Set the board to be full of dictionaries
            for column in range(1,size+1):
                self.board[row][column] = "EMPTY" ##Initialize to empty
                
    def getLocation(self, row, col):
        return self.board(row,col)
        
    def setLocation(self, row, col, piece):
        if self.board[row][col] == "EMPTY":
            self.board[row][col] = piece
            return 0    #good, piece was set correctly
        else:
            print "bad move"
            return -1
            
    def movePieceFrom(rowOrig, colOrig, rowNew, ColNew, piece):
        print "finish this later"
            
    def printBoard(self):
        print "---Piece---------| Row |---| Column |---"
        for row in self.board.keys():
            for col in self.board[row].keys():
                if self.board[row][col] != "EMPTY":
                    print self.board[row][col].printPiece(), "  ", row, "\t\t", col   ##if it is not "empty" then it is a piece, print that shit
                    ##print "FALSE"   #there ain't shit here! Removed the print, just clutters shit up brah!
        
