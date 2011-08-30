class board:
    """
    The board class will be a dictionary of dictionaries.
    Each access at the top level will be the row, each access afterwards
    will be the column.
    Ex: globalBoard = board(8) #returns a board of size 8x8
    print globalBoard.getLocation(1,1)  #will either print NIL or a piece (if it is there)
    """
    def getLocation(self, row, column):
        return self.boardInfo[row][column]

    def __init__(self, rows):
        self.boardInfo = {}
        for rowNum in range(1, rows):
            self.boardInfo[rowNum] = {}
            for column in range(1,rows):
                self.boardInfo[rowNum][column] = column
