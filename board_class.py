##Example: {1 : 1} would denote row 1, column 1
##Example 2: {{1 : 1}
class board(dict):
    """initializing a board class..."""
    def __init__(self, size):
        for row in range(1,size+1):
            self[row] = {}                  ##Set the board to be full of dictionaries
            for column in range(1,size+1):
                self[row][column] = "EMPTY" ##Initialize to empty
                
    
a = board(10)
