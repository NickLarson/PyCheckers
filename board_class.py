##We'll use the Python equivilant to AutoVification (Thanks Perl!) ^_^
##Example: {1 : 1} would denote row 1, column 1
##Example 2: {{1 : 1}
class board(dict):
    """initializing a board class using AutoVivication"""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
    def __init__(self, rows):
        for row in range(1,rows+1):
            if row != (rows/2) and row != (rows/2)-1:         ##We need to keep track of fully empty rows
                if row%2 == 0:                        ##Odd row, odd column vice versa
                    for col in range(1,rows+1):
                        if col%2 == 0:
                            self[row][col] = '0'
                        else:
                            self[row][col] = 'X'
                else:                             ##This does the inverse... just fills it in backward
                    for col in range(1,rows+1):
                        if col%2 == 0:
                            self[row][col] = 'X'
                        else:
                            self[row][col] = '0'
            else:
                for col in range(1,rows+1):    ##This will fill in the blank middle space... thus the rows/2 and rows/2-1
                    self[row][col] = '0'
a = board(10)

#board[row][column]
#This worked when I took init out, it's basically the same just not a member
def initialize(board, rows):
    blank = rows/2
    blank2 = blank-1
    print blank2
    print blank
    for row in range(1,rows+1):
        if row != (rows/2) and row != (rows/2)-1:         ##We need to keep track of fully empty rows
            if row%2 == 0:                        ##Odd row, odd column vice versa
                for col in range(1,rows+1):
                    if col%2 == 0:
                        board[row][col] = '0'
                    else:
                        board[row][col] = 'X'
            else:
                for col in range(1,rows+1):
                    if col%2 == 0:
                        board[row][col] = 'X'
                    else:
                        board[row][col] = '0'
        else:
            ##print row == rows/2
            for col in range(1,rows+1):
                board[row][col] = '0'

def printBoard(board, row):
    if row <= 10:
        print a[row]
        printBoard(board, row+1)

printBoard(a, 1)

##This returns true where all of the positions are filled in with a piece (Denoted by 'X')
def test():
    for y in range(1,11):
        if a[1][y] == 'X':
            print "True at position", y, "Row 1"
