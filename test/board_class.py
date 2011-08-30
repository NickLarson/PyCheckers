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

a = board()

def initialize(board):
    for row in range(1,11):
        if row%2 == 0:
            for column in range(1,11):
                board[column][row] = 'X'
        else:
            for column in range(1,11):
                board[column][row] = '0'


def printBoard(board):
    for x in range(1,11):
        print "----Row ", x, "----"
        print board[x]


##This returns true where all of the positions are filled in with a piece (Denoted by 'X')
for y in range(1,11):
    if a[1][y] == 'X':
        print "True at position", y, "Row 1"
